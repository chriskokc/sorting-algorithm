# merge sort
# divide and conquer


def merge_sort(arr):
    if len(arr) > 1:
        # divide the array into two sub-arrays
        mid = len(arr) // 2
        l_sub_arr = arr[:mid]
        r_sub_arr = arr[mid:]
        # get them sorted by doing recursion
        merge_sort(l_sub_arr)
        merge_sort(r_sub_arr)
        # compare the head of L and the head of R
        # we now have three arrays: l, r and the original arr
        i = 0
        l_head = 0
        r_head = 0
        while l_head < len(l_sub_arr) and r_head < len(r_sub_arr):
            # merge by overwriting the original array
            if l_sub_arr[l_head] < r_sub_arr[r_head]:
                arr[i] = l_sub_arr[l_head]
                l_head += 1
            else:
                arr[i] = r_sub_arr[r_head]
                r_head += 1
            i += 1
        # if one is exhausted
        while l_head < len(l_sub_arr):
            arr[i] = l_sub_arr[l_head]
            l_head += 1
            i += 1
        while r_head < len(r_sub_arr):
            arr[i] = r_sub_arr[r_head]
            r_head += 1
            i += 1









