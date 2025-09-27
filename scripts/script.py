from modules import firstsubmodule, secondsubmodule

print("the following output will be from the first submodule. it should say 'i'm running'")
firstsubmodule.run()

print("the following output will be from the second submodule. it should say 'my name is function'")
firstsubmodule.second_function()

print("the following output will be from the second submodule. it should say 'what nice functions you have!''")
secondsubmodule.a_function_for_the_third()
