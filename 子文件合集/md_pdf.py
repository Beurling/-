import pypandoc
# import pandoc
import os
# import pandoc
# os.system('pandoc -o test.md text.html')
# 转换md md可以转word了
# pypandoc.convert_file('test.md', 'pptx', format='md', outputfile='test.pptx')
pypandoc.convert_file('test2.ipynb', 'docx', format='ipynb', outputfile='test2.docx')
# 不能输入ppt
# pypandoc.convert_file('test.pptx', 'docx', format='pptx', outputfile='test_1.docx')
