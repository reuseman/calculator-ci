from flakon import JsonBlueprint
from flask import request, jsonify
from myservice.calculator import calculator as c


calc = JsonBlueprint("calc", __name__)


@calc.route("/calc/sum", methods=["GET"])
def sum():
    m = int(request.args.get("m"))
    n = int(request.args.get("n"))

    result = c.sum(m, n)

    return jsonify({"result": str(result)})


@calc.route("/calc/sub", methods=["GET"])
def sub():
    m = int(request.args.get("m"))
    n = int(request.args.get("n"))

    result = c.subtract(m, n)

    return jsonify({"result": str(result)})


@calc.route("/calc/mul", methods=["GET"])
def mul():
    m = int(request.args.get("m"))
    n = int(request.args.get("n"))

    result = c.multiply(m, n)

    return jsonify({"result": str(result)})


@calc.route("/calc/div", methods=["GET"])
def div():
    m = int(request.args.get("m"))
    n = int(request.args.get("n"))

    if n == 0:
        return jsonify({"result": str("DivisionByZeroError")})

    result = c.divide(m, n)

    return jsonify({"result": str(result)})
