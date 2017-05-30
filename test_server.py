from server import new_instance, COMMON_DEFAULT_ATTRIBUTES

def test_no_preexisting():
    instance = new_instance("test")
    assert instance["host_name"] == "test-1.domain.com"
    assert instance["attributes"] == COMMON_DEFAULT_ATTRIBUTES

def test_preexisting_continuous_index():
    instance = new_instance("test", ["test-1.domain.com"])
    assert instance["host_name"] == "test-2.domain.com"
    assert instance["attributes"] == COMMON_DEFAULT_ATTRIBUTES

def test_preexisting_noncontinuous_index():
    instance = new_instance("test", [
        "test-1.domain.com",
        "test-2.domain.com",
        "test-4.domain.com"
        ])
    assert instance["host_name"] == "test-3.domain.com"
    assert instance["attributes"] == COMMON_DEFAULT_ATTRIBUTES

def test_prexisting_continuous_index_above_1():
    instance = new_instance("test", [
        "test-5.domain.com",
        "test-65.domain.com",
        "test-4.domain.com"
        ])
    assert instance["host_name"] == "test-1.domain.com"
    assert instance["attributes"] == COMMON_DEFAULT_ATTRIBUTES


