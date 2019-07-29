import sys
import cwd_module
try:
    import tree_module
except ModuleNotFoundError as why:
    print('tree_module not added in sys.path yet: {}'.format(why))

sys.path.append('cannot_find')
print(sys.path[-1])
import tree_module

print(cwd_module.msg())
print(tree_module.msg())
