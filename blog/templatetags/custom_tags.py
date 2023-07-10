from django import template
from django.template.defaultfilters import stringfilter
from django.utils.safestring import SafeString,mark_safe
from django.utils.html import conditional_escape

register=template.Library()

# template filters

@register.filter(name='replace_word')
def replace_arg(value,args):
	arg1,arg2=args.split(',')
	return value.replace(arg1,arg2)
@register.filter(name='append_x')
def add_x(value):
	return f'{value}+x'


@stringfilter
@register.filter(name='upper')
def stringify_upper(value):
	upper=value.upper()
	return f'type of ({upper}) is {type(value)}'

@register.filter
def is_safe_string(value):
	if isinstance(value,SafeString):
		return f'({value}) is SafeString'
	else:
		return f'({value}) is not SafeString'


@register.filter
def safe_to_normal(value):
	value=f'word added to safestring:{value}'
	return value



@register.filter(is_safe=True)
def safe_again(value):
	value=f'word added to safestring:{value}'
	return value

@register.filter(needs_autoescape=True)
def needs_autoescape(value,autoescape=True):
  """
  Escapes the given value, depending on the current auto-escaping state.
  """
  if autoescape:
    return conditional_escape(value)
  else:
    return value

@register.filter
def without_needs_autoescape(value,autoescape=True):
  """
  Escapes the given value, depending on the current auto-escaping state.
  """
  if autoescape:
    return conditional_escape(value)
  else:
    return value


@register.filter(needs_autoescape=True)
def cond_escape(value,autoescape=True):
  """
  Escapes the given value, depending on the current auto-escaping state.
  """
  if autoescape:
    return conditional_escape(value)
  else:
    return value


# template tag

# simple tag

#simple tag with lambda
register.simple_tag(lambda x:x-1,name='minusone')

#simple tag with takes_context
@register.simple_tag(takes_context=True)
def say_name(context):
	return f'{context["name"]} is my name'
