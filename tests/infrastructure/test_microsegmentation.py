from infrastructure.network.microsegmentation import vlan_shift_asset
import pytest

def test_vlan_shift_asset_success():
    assert vlan_shift_asset("host1") is True

def test_vlan_shift_asset_failure():
    with pytest.raises(Exception):
        vlan_shift_asset("fail")
