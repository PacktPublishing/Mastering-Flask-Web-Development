from modules.external import external_bp
from numpy import array
from modules.external.services.julia_transactions \
    import return_result, return_words, total_array, total_map


@external_bp.route('/julia/<int:x>/<int:y>')
async def juliaexp(x, y):
    
    data = [10, 30, 40, 50]
    data = await return_result(x, y)
    print(data)
   
    words = await return_words("[a-zA-Z]+","PythonCall.jl is very useful")
    print(words)

    total = await total_array([1, 4, 5, 10, 12])
    print(total)
    
    dataf = [[1, 2, 3, 4],
             [20, 21, 19, 18]
    ]
 
    # Create DataFrame
    df = array(dataf)
    print(df)
   
    total = await total_map(df)
    print(total)
    return "result"