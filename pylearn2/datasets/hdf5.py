"""Objects for datasets serialized in HDF5 format (.h5)."""
import tables
from pylearn2.datasets.dense_design_matrix import DenseDesignMatrix


class HDF5Dataset(DenseDesignMatrix):
    """Dense dataset loaded from an HDF5 file."""
    def __init__(self, filename, X=None, topo_view=None, y=None, **kwargs):
        """
        Loads data and labels from HDF5 file.

        Parameters
        ----------
        filename: str
            HDF5 file name.
        X: str
            Key into HDF5 file for dataset design matrix.
        topo_view: str
            Key into HDF5 file for topological view of dataset.
        y: str
            Key into HDF5 file for dataset targets.
        kwargs: dict
            Keyword arguments passed to `DenseDesignMatrix`.
        """
        with tables.File(filename) as f:
            if X is not None:
                if not X.startswith('/'):
                    X = "/" + X
                X = f.get_node(X)[:]
            if topo_view is not None:
                if not topo_view.startswith('/'):
                    topo_view = "/" + topo_view
                topo_view = f.get_node(topo_view)[:]
            if y is not None:
                if not y.startswith('/'):
                    y = "/" + y
                y = f.get_node(y)[:]

        super(HDF5Dataset, self).__init__(X=X, topo_view=topo_view, y=y,
                                          **kwargs)
