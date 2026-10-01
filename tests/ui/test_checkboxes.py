import pytest

@pytest.mark.smoke
@pytest.mark.ui
def test_checkboxes_page_loads(checkboxs_page):
    """Checkboxes page loads with 2 checkboxes"""
    checkboxs_page.open()
    boxes = checkboxs_page.get_all_checkboxes()
    assert len(boxes)==2

@pytest.mark.regression
@pytest.mark.ui
def test_check_all(checkboxs_page):
    """All checkboxes can be checked"""
    checkboxs_page.open()
    checkboxs_page.check_all()
    assert checkboxs_page.get_checked_count() == 2

@pytest.mark.regression
@pytest.mark.ui
def test_uncheck_all(checkboxs_page):
    """All checkboxes can be unchecked"""
    checkboxs_page.open()
    checkboxs_page.uncheck_all()
    assert checkboxs_page.get_checked_count() == 0



