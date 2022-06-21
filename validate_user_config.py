allowed_options = {
        "operation": {"venta", "alquileres", "alquileres-temporarios", "tiempo-compartido", "compra"},
        "currency": {"pesos", "dolares"},
}

def assert_valid_data(config: dict):
    assert_allowed_options(config, allowed_options)
    assert_valid_format(config)

def assert_allowed_options(config: dict, allowed_options: dict):
    for option, allowed_options in allowed_options.items():
        assert config.get(option) in allowed_options

def assert_valid_format(config: dict):
    for option in config.values():
        if type(option) is list:
            for item in option:
                assert_valid_string(item)
        else:
            assert_valid_string(option)

def assert_valid_string(string):
    assert " " not in string # string shouldn't have spaces
    assert  string.isalnum() or string.islower() # string should be lowercase


