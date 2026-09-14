# pylint: disable=missing-module-docstring,missing-class-docstring,missing-function-docstring,duplicate-code,too-many-locals
from piemakerlibexample import Display

display = Display(conf_files=['piemakerlibexample.yaml'])
text = display.format(reverse=False, transformation='lower')
print(text)