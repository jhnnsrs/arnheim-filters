import xarray as xr
from larvik.consumers import LarvikError

from larvik.helpers import LarvikParser, LarvikManager


class MaxISP(LarvikParser):

    @staticmethod
    def filter(array: xr.DataArray, settings: dict, manager = LarvikManager()) -> xr.DataArray:
        if "z" not in array.dims: raise LarvikError("The Data has no Z Dimensions")
        return array.max(dim="z", keep_attrs=True)


class SlicedMaxISP(LarvikParser):

    @staticmethod
    def filter(array: xr.DataArray, settings: dict, manager = LarvikManager()) -> xr.DataArray:
        lowerBound: int = int(settings.get("lowerBound", -1))
        upperBound: int = int(settings.get("upperBound", -1))

        array = array.sel(z=slice(lowerBound, upperBound)).max(dim="z")

        return array