import dask.array as da
import pytest
import xarray as xr
from larvik.consumers import LarvikError
from larvik.helpers import LarvikManager

from .consumers import MaxISPConsumer


manager = LarvikManager()
# Create your tests here.
def mockArrays():
    dims = ["x","y","c","z","t"]
    shape = (1024,1024,3,20,20)

    arrays = []
    runlist = []
    for index, dim in enumerate(dims):
        runlist += [dim]
        array = da.zeros(shape[:index+1])
        dummy = xr.DataArray(array, dims=runlist)
        arrays.append(dummy)

    return arrays



def test_maxisp():
    arrays = mockArrays()
    for array in arrays:
        if "z" in array.dims:
            maxisp = MaxISPConsumer.filter(array, {}, manager)
            assert "z" not in maxisp.dims
        else:
            with pytest.raises(LarvikError):
                MaxISPConsumer.filter(array, {}, manager)