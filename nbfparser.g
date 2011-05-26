#
# ----------------------------------------------------------------------------
# "THE BEER-WARE LICENSE" (Nicolas V custom edition):
# Nicolas V wrote this file. As long as you retain this notice you
# can do whatever you want with this stuff. But please say it's me that did it,
# because I seek for eternal glory. If we meet some day, and you think
# this stuff is funny, you can buy me a beer in return.
# ----------------------------------------------------------------------------
#

parser NoBrainFuck:

ignore: "\\s+"
ignore: "\\#[^\n]*"
token incrementp: "[hH]+[oO]+"
token decrementp: "[hH]+[aA]+"
token increment: "[Yy]+[eE]+[sS]+"
token decrement: "[Nn]+[oO]+"
token prints: "[Mm]+[Yy]+\\s+[Gg]+[Oo]+[dD]+"
token accepts: "[hH]+[aA]+[rR]+[dD]+[eE]+[rR]+"
token begins: "[Nn]+[Oo]+[tT]+\\s+[Yy]+[eE]+[Tt]+"
token ends: "[Ii]+'+[Mm]+\\s+[Cc]+[Oo]+[Mm]+[Ii]+[Nn]+[Gg]+"

rule program: {{ tmp = "" }} (expression {{ tmp = tmp + expression }})* "$" {{ return tmp }}
rule expression: incrementp {{ return ">" }} | decrementp {{ return "<" }} | increment {{ return "+" }} |
    decrement {{ return "-" }} | prints {{ return "." }} | accepts {{ return "," }} | begins {{ return "[" }} |
    ends {{ return "]" }}

