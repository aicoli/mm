list = ["ad", "ab", "ac"]
print("原始列表:", list)
print("\n访问元素:")
print("第一个元素:", list[0])
print("第二个元素:", list[1])
print("最后一个元素:", list[-1])
print("\n--- 添加元素 ---")          #添加元素两种方法
list.append("af")
print("使用 append() 后:", list)
list.extend(["ag", "af"])
print("使用 extend() 后:", list)
print("\n--- 修改元素 ---")       #修改列表元素
list[2] = "ae"
print("修改索引2后:", list)
print("\n--- 删除元素 ---")          #删除元素三种方法
list.remove("ab")
print("使用 remove() 后:", list)
removed_item = list.pop(1)
print(f"使用 pop(1) 删除的元素: {removed_item}, 剩余列表:", list)
del list[1]
print("使用 del 删除索引1后:", list)
