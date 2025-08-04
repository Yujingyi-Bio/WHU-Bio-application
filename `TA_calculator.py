```python
# 计算DNA序列TA含量
def ta_content(sequence):
    return (sequence.count("T") + sequence.count("A")) / len(sequence) * 100
print("TA含量计算器已就绪！)
