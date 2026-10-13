def parse_student(line):
    fields = line.strip().split(",")
    if len(fields) != 2:
        raise ValueError("记录必须包含姓名和成绩两个字段")

    name = fields[0].strip()
    if not name:
        raise ValueError("姓名不能为空")

    try:
        score = int(fields[1].strip())
    except ValueError as error:
        raise ValueError("成绩必须是整数") from error

    if not 0 <= score <= 100:
        raise ValueError("成绩必须在 0 到 100 之间")

    return {"name": name, "score": score}