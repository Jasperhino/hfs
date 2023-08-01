import pytest

from ..feature_selection import EagerHierarchicalFeatureSelector
from .fixtures.fixtures import wrong_hierarchy_X, wrong_hierarchy_X1


@pytest.mark.parametrize(
    "data",
    [wrong_hierarchy_X(), wrong_hierarchy_X1()],
)
def test_HierarchicalFeatureSelector(data):
    X, hierarchy, columns = data
    selector = EagerHierarchicalFeatureSelector(hierarchy)
    with pytest.warns(UserWarning):
        selector.fit(X, columns=columns)
