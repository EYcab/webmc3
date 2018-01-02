def get_varnames(trace, include_transformed=False):
    return [
        {
            'label': varname,
            'value': varname
        }
        for varname in trace.varnames
        if not varname.endswith('__') or include_transformed
    ]
