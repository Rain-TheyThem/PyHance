from yapf.yapflib.yapf_api import FormatFile

for file in ("bytes_to", "dict", "haversine", "list", "range", "string", "typechecks"):
    FormatFile(f"pyhance/{file}.py", in_place=True)