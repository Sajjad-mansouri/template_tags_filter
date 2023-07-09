from django import template
from django.template.defaultfilters import stringfilter
from django.utils.safestring import SafeString

register=template.Library()

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

