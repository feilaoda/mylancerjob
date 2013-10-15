#!/usr/bin/env python
# -*- coding: utf-8 -*- 

from urlparse import urlparse
import itertools
import re

def compile_regex(regex):
    try:
        return re.compile(regex, re.I)
    except Exception, e:
        raise Exception("invalid regex " + regex + " : " + str(e))
    
def execute_pattern(rule, url):
    patterns = rule.get('patterns_re')
    if patterns is None:
        patterns = dict((pname, compile_regex(rule[pname])) for pname in ('pattern', 'qpattern', 'hpattern', 'spattern') if pname in rule)
    
    groups = dict()
    if 'spattern' in patterns:
        m = patterns['spattern'].search(url.scheme)
        if not m: return None
        groups.update(m.groupdict())
    if 'hpattern' in patterns:
        m = patterns['hpattern'].search(url.hostname)
        if not m: return None
        groups.update(m.groupdict())
    if 'pattern' in patterns:
        m = patterns['pattern'].search(url.path)
        if not m: return None
        groups.update(m.groupdict())
    if 'qpattern' in patterns:
        m = patterns['qpattern'].search(url.query)
        if not m: return None
        groups.update(m.groupdict())
    return groups

def execute_rule(rule, url):
    if 'execute' in rule:
        return rule['execute'](url)
    
    m = execute_pattern(rule, url)
    if m is None: return ()
    
    rule_name = rule.get('name')
    if not rule_name: raise Exception('missing name in rule ' + rule)
    ret = [('rule', rule_name)]
    ret.extend(m.items())
    #ret.extend([(k,urllib.unquote_plus(v)) for k,v in m.groupdict().iteritems()])
    return ret

def execute_param(rule, url):
    if 'execute' in rule:
        return rule['execute'](url)
    
    m = execute_pattern(rule, url)
    if m is None: return ()

    return m.items()

def execute_rules(mod, url):
    urlp = urlparse(url, allow_fragments=False)
    if not mod.__dict__['match'](urlp): return None
    
    rules = mod.__dict__.get('rules')
    if not rules: raise Exception('rules not found in mod.__name__')
        
    the_rule = None
    for rule in mod.__dict__['rules']:
        rule_result = execute_rule(rule, urlp)
        if rule_result:
            the_rule = rule
            break

    params = mod.__dict__.get('params')
    params_result = itertools.chain.from_iterable((execute_param(rule, urlp) for rule in params)) if params else ()
    
    ret = dict(itertools.chain(rule_result, params_result))
    
    if the_rule:
        action = rule.get('action')
        if action: ret['action'] = action
    
        norm = rule.get('norm')
        if norm: 
            try:
                ret['norm'] = norm.format(**ret)
            except:
                pass     
    
    return ret

def verify_example(name, expected, actual):
    errors = []
    if not actual:
        return ('not matched') if expected else ()
    for k,v in expected.iteritems():
        if k not in actual:
            errors.append(k + ': not found in actual')
        elif v != actual[k]:
            errors.append(k + ': expected {0}, found {1}'.format(v, actual[k]))
            del actual[k]
    for k,v in actual.iteritems():
        if k not in expected:
            errors.append(k + ': not found in expected')
    return None if not errors else errors
    
def test_examples(name):
    mod = __import__(name, globals(), locals(), ['*'], -1)
    
    examples = mod.__dict__.get('examples')
    if not examples: return True
    
    results = (execute_rules(mod, url) for url,_ in examples)
    verify = ((expected[0], verify_example(name, expected[1], actual)) for expected, actual in itertools.izip(examples, results))
   
    ret = True
    for url,v in verify:
        if v:
            print url, v
            ret = False
    return ret
        
      
if __name__ == "__main__":
    print test_examples('newegg')
