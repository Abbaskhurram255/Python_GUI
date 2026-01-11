from typing import Any, Self
from numbers import Number
import builtins

__old_list__ = builtins.list
class Arr(__old_list__):
    def __init__(self, *objs):
        super().__init__()
        self.push(objs)
    def filter_out(self, fn):
        if not callable(fn):
            return None
        self[:] = [x for x in self if not fn(x)]
        return self
    def keep_if(self, fn):
        if not callable(fn):
            return None
        self[:] = [x for x in self if fn(x)]
        return self
    def map(self, fn):
        if not callable(fn):
            return None
        self[:] = [fn(x) for x in self]
        return self
    def unique(self):
        self[:] = __old_list__(dict.fromkeys(self))
        return self
    def has(self, x):
        return x in self
    def includes(self, x):
        return self.has(x)
    def i(self, i, default=None):
        if not isinstance(i, int):
            return None
        if i < 0:
            i = len(self) + i
        if 0 <= i < len(self):
            return self[i]
        return default
    def last(self):
        if self:
            return self[-1]
        return None
    def last_i(self, n):
        if not isinstance(n, int):
            return None
        if n > 0 and n <= len(self):
            return self[-n]
        return None
    def nth(self, n):
        return self.i(n)
    def nth_last(self, n):
        return self.last_i(n)
    def first(self):
        if self:
            return self[0]
        return None
    def second(self):
        return self.i(1)
    def sec_last(self):
        return self.last_i(2)
    def update(self, i, x):
        if not isinstance(i, int):
            return None
        if i < 0:
            i = len(self) + i
        if 0 <= i < len(self):
            self[i] = x
        return self
    def replace(self, i, x):
        return self.update(i, x)
    def shuffle(self):
        import random
        if len(self) > 1:
            random.shuffle(self)
        return self
    def sort(self, key=None, reverse=False):
        if len(self) > 1:
            super().sort(key=key, reverse=reverse)
        return self
    def reverse(self):
        if len(self) > 1:
            super().reverse()
        return self
    def key_array(self):
        return __old_list__(range(len(self)))
    def keys(self):
        return self.key_array()
    def values(self):
        return __old_list__(self)
    def entries(self):
        return [self.keys(), self.values()]
    def __str__(self):
        return f"Arr({super().__str__()})"
    def slice(self, start: int = None, stop: int = None):
        if not isinstance(start, int) or not isinstance(end, int) or start >= len(self) or end > len(self) or start == end:
        	return self[:]
        return Arr(self[start:stop])
    def slice_keep(self, x):
        if not isinstance(x, int) or x <= len(self) or x > len(self):
        	return self.copy()
        return self.slice(0, x)
    def slice_right(self, x):
        if not isinstance(x, int):
        	return self.copy()
        return self.slice(len(self) - x)
    def slice_end(self, x):
        if not isinstance(x, int):
        	return self.copy()
        return self.slice(0, len(self) - x)
    def random(self):
        import random
        if self:
            return random.choice(self)
        return None
    def empty(self) -> Self:
        self.clear()
        return self
    def eq(self, other):
        if not isinstance(other, __old_list__):
        	return False
        return self.array() == other.array()
    def compare(self, other):
        if not isinstance(other, __old_list__):
        	return False
        intersection = Arr(set(self.array()) & set(other.array()))
        return len(intersection) > len(self.array()) / 2
    def union(self, *arrays):
        return self.combine(*arrays)
    def cat(self, *arrays):
        return self.combine(*arrays)
    def concat(self, *arrays):
        return self.combine(*arrays)
    def join(self, *arrays):
        return self.combine(*arrays)
    def join_str(self, s: str = ""):
        return str(s).join(map(str, self))
    def intersection(self, *arrays):
        for arr in arrays:
            if isinstance(arr, __old_list__):
                self[:] = [x for x in self if x in arr]
            elif isinstance(arr, Arr):
                self[:] = [x for x in self if x in arr]
        return self
    def negative_intersection(self, *arrays):
        for arr in arrays:
            if isinstance(arr, __old_list__):
                self[:] = [x for x in self if x not in arr]
            elif isinstance(arr, Arr):
                self[:] = [x for x in self if x not in arr]
        return self
    def map_val(self, old_val, new_val) -> Self:
        for i, x in enumerate(self):
            if x == old_val:
                self[i] = new_val
        return self
    def sum(self) -> Number:
    	if not len(self):
    		return 0.0
    	nums: __old_list__[Number] = [num for num in self if num is not None and isinstance(num, Number)]
		# this is a necessary check
    	if not len(nums):
		    return 0.0
    	return sum(nums)
    def difference(self) -> Number:
    	if not len(self):
    		return 0.0
    	nums: __old_list__[Number] = [num for num in self if num is not None and isinstance(num, Number)]
		# this is a necessary check
    	if not len(nums):
		    return 0.0
    	diff: Number = nums[0]
    	for i, item in old_enumerate(nums):
        	if i == 0:
        		continue
			# since we've already taken care of the first item
			# we don't that
	        if item > 1e9:
		        item = 1e9
	        if item < 1e-9:
		        item = 1e-9
	        diff -= item
    	return diff
    diff = difference
    def product(self) -> Number:
	    if not len(self):
		    return 0.0
	    nums: __old_list__[Number] = [num for num in self if num is not None and isinstance(num, Number)]
		# this is a necessary check
	    if not len(nums):
		    return 0.0
	    prd: Number = nums[0]
	    for i, item in old_enumerate(nums):
		    if i == 0:
		        continue
			# since we've already taken care of the first item
			# we don't that
		    if item > 1e9:
		    	item = 1e9
		    if item < 1e-9:
		    	item = 1e-9
		    prd *= item
	    return prd
    prd = product
    def quotient(self) -> Number:
	    if not len(self):
		    return 0.0
	    nums: __old_list__[Number] = [num for num in self if num is not None and isinstance(num, Number)]
		# this is a necessary check
	    if not len(nums):
		    return 0.0
	    quo: Number = nums[0]
	    for i, item in old_enumerate(nums):
		    if i == 0:
		    	continue
			# since we've already taken care of the first item
			# we don't that
		    if item == 0:
		    	item = 1
		    if item > 1e9:
		    	item = 1e9
		    if item < 1e-9:
		    	item = 1e-9
		    quo /= item
	    return quo
    quo = quotient
    def max(self) -> Number:
	    if not len(self):
		    return 0.0
	    nums: __old_list__[Number] = [num for num in self if num is not None and isinstance(num, Number)]
		# this is a necessary check
	    if not len(nums):
		    return 0.0
	    return max(nums)
    def min(self) -> Number:
	    if not len(self):
		    return 0.0
	    nums: __old_list__[Number] = [num for num in self if num is not None and isinstance(num, Number)]
		# this is a necessary check
	    if not len(nums):
		    return 0.0
	    return min(nums)
    def combine(self, *args) -> Self:
	    if not args:
		    return self
	    for arg in args:
	    	if isinstance(arg, tuple):
	    		arg = __old_list__(arg)
				# a tuple?
				# no thanks,
				# we need a list
	    	if isinstance(arg, __old_list__):
	    	    self.extend(arg)
	    	else:
	    	    self.append(arg)
	    return self
    add = push = combine
    def push_at(self, i: int, *items) -> Self:
	    if not len(items):
		    return self
	    if not isinstance(i, int):
		    i = len(self)
	    if i < 0:
	    	i = 0
	    elif i > len(self):
	    	i = len(self)
	    #items = flatten(__old_list__(items))
	    x = self[:i] + __old_list__(items) + self[i+len(items)-1:]
	    updated_list: __old_list__ = __old_list__(x)
	    self.clear()
	    self.extend(updated_list)
	    return self
    def push_start(self, *items) -> Self:
	    self.push_at(0, *items)
	    return self
    unshift = push_start
    def shift(self) -> Any|None:
	    if len(self) == 0:
	    	return None
	    return self.pop(0)
	    # pop the first item, "shift"ing all to the left by one bit
	# OVERRIDE self.remove
    old_remove = __old_list__.remove
    def remove(self, *items) -> Any|None:
	    if not len(self):
	    	return None
	    if not len(items):
	    	return super().pop()
	    items = flatten(__old_list__(items))
	    last_removed: Any = items[-1]
	    for item in items:
	    	if not self.contains(item):
	    		continue
	    	self.old_remove(item)
	    return last_removed
    rmv = remove
	# OVERRIDE self.pop
    old_pop = __old_list__.pop
    def pop(self, *items) -> Any|None:
	    if not len(self):
	    	return None
	    if not len(items):
	    	return super().pop()
	    items = flatten(__old_list__(items))
	    last_popped: Any = self.old_pop(items[-1])
	    for index in items:
	    	if index >= len(self):
	    		continue
	    	if index < 0:
	    		index = len(self) - abs(index)
	    		if index < 0 or index >= len(self):
	    			continue
	    	self.old_pop(index)
	    return last_popped
    def contains(self, item) -> bool:
	    return self.count(item) > 0
    has = includes = contains
    def index_of(self, x: Any) -> int:
	    if not self.contains(x):
	    	return -1
	    return self.index(x)
    find = find_index = index_of
    no_of = counts_of = __old_list__.count
    def print_map(self):
        print(self.array())
    def length(self):
        return len(self)
builtins.list = Arr
print(list)
        
arr: list = list(1, 3, 5, "x")
arr.pop()
arr.push_at(50, 3, 7, 9, 11)
print(arr.unique().sort())
print(arr.sum())