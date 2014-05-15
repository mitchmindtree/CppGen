" 
" CppGen.vim
"
" by Mitchell Nordine
"
" Generate .cpp and .h file pairs from your own template!
"
"   :CppGen 'name1' 'name2' 'name3'  =  name1.cpp, name1.h, name2.cpp, etc
"

function CppGenerate(dir, ...)
    let names=""
    for s in a:000
        let names=names . " " . s
    endfor
    execute "!python ~/.vim/plugin/CppGen/CppGen.py " . " " . a:dir . " " . names
endfunction

com -nargs=* CppGen call CppGenerate(getcwd(), <f-args>)
    

