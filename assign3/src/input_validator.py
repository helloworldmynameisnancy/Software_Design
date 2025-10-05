def input_validator(func):
    def validate_input_and_call(number, *args, **kwargs):
        if number < 0:     
            raise ValueError("Factorials of negative numbers are undefined.")
        
        return func(number, *args, **kwargs)

    return validate_input_and_call
