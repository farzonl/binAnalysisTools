# Binary Analysis Tools

# Tools 
- dff 
    - why is it called dff?: b\c I have a `diff` alias in my `.bashrc`.
    - how to use? `python dff.py bin1 bin2`
    - why does this exist? 
    Mach-O binaries are fat binaries and need seperate diffing of sections and symbols. So an objdump section size diff will be different fron a strings diff. Elf doesn't have this problem b\c `.rodata` shows up in sections and doesn't have a seperate partition for symbols\strings.
- More Tools to be added.