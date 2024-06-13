module Ch06JuliaPkg

using PythonCall
using Statistics
import DataFrames
import Pandas


const re = PythonCall.pynew() # import re
const np = PythonCall.pynew() # import numpy

function __init__()
    PythonCall.pycopy!(re, pyimport("re"))
    PythonCall.pycopy!(re, pyimport("numpy"))
end

function return_wrds(wrds, strdata) 
    return re.findall(wrds, strdata)
end

function g(x, y)
    result = y * √x
    return result
end

function f(x, y)
    result = x + y
    return result
end

function sum_array(data_list)
    total = 0
    for n in eachindex(data_list)
         total = total + data_list[n]
    end
    return total
end

function sum_map(datadict)
    
    df_julia = DataFrames.DataFrame(datadict, ["col1", "col2", "col3", "col4"])
    rows = DataFrames.nrow(df_julia)
    array = Matrix(df_julia,[:,1:3])
    return 0
end

export f, g, return_wrds, sum_array, sum_map

end # module Ch06JuliaPkg

#julia --project=C:\Alibata\Training\Source\flask\mastering\ch06-web-final\Ch06JuliaPkg