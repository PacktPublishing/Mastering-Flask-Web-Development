
import juliacall
from juliacall import Pkg as jlPkg
from pandas import DataFrame
#from juliacall import Main as jl3
jlPkg.activate(".\\Ch06JuliaPkg") 
jl = juliacall.newmodule("modules.external.services")
jl.seval("using Pkg")
jl.seval("Pkg.instantiate()")
jl.seval("using Ch06JuliaPkg")
jl.seval("using DataFrames")
jl.seval("using PythonCall")


async def return_result(x, y):
    result = jl.seval(f"f({x}, {y})")
    #jl3.seval(f"greet()")
    #jl3.seval(f"make_range()")
    print(jl.seval(f"g({x}, {y})"))
    return result

async def return_words(rule, wrds):
   result = jl.seval(f'return_wrds("{rule}", "{wrds}")')
   return result

async def total_array(arrdata):
    result = jl.seval(f"sum_array({arrdata})")
    return result

async def total_map(arrmap):
    #df_julia = jl3.convert(jl3.PyTable, arrmap)
    #print(df_julia)
    #data_dict = jl3.seval("Dict({arrmap})")
    #print(data_dict)
    
    result = jl.seval(f"sum_map({arrmap})")
   
    return result