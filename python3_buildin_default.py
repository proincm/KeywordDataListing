__import__ | abs | all | any | ascii | basestring | bin | bool |
          bytearray | bytes | callable | chr | classmethod | cmp | compile |
          complex | delattr | dict | dir | divmod | enumerate | eval | exec |
          execfile | file | filter | float | format | frozenset | getattr |
          globals | hasattr | hash | help | hex | id | input | int |
          isinstance | issubclass | iter | len | list | locals | long | map |
          max | memoryview | min | next | object | oct | open | ord | pow |
          property | range | raw_input | reduce | reload | repr |
          reversed | round | set | setattr | slice | sorted | staticmethod |
          str | sum | super | tuple | type | unichr | unicode | vars |
          xrange | zip

          
          magic_function_calls:
    patterns:
    - name: meta.function-call.python
      begin: |-
        (?x)
          (\.)?
          \b(
            __(?:
              abs | add | aenter | aexit | aiter | and | anext | await | bool |
              bytes | call | ceil | cmp | coerce | complex | contains | copy |
              deepcopy | del | delattr | delete | delitem | delslice | dir | div |
              divmod | enter | eq | exit | float | floor | floordiv | format | ge |
              get | getattr | getattribute | getinitargs | getitem | getnewargs |
              getnewargs_ex | getslice | getstate | gt | hash | hex | iadd | iand |
              idiv | idivmod | ifloordiv | ilshift | imatmul | imod | imul | index |
              init | instancecheck | int | invert | iop | ior | ipow | irshift |
              isub | iter | itruediv | ixor | le | len | length_hint | long |
              lshift | lt | matmul | missing | mod | mul | ne | neg | new | next |
              nonzero | oct | op | or | pos | pow | prepare | radd | rand | rcmp |
              rdiv | rdivmod | reduce | reduce_ex | repr | reversed | rfloordiv |
              rlshift | rmatmul | rmod | rmul | rop | ror | round | rpow | rrshift |
              rshift | rsub | rtruediv | rxor | set | setattr | setitem | setslice |
              setstate | sizeof | str | sub | subclasscheck | truediv | trunc |
              unicode | xor)
            __)
          \s*(?=(\())
