from app.robots.IFR2 import IFR2

def robotDTO(robot):
    if robot['_cls'] == "RobotSchema.IFR2Schema":
        robot['type'] = "IFR2"
    elif robot['_cls'] == "RobotSchema.CrossAverageSchema":
        robot['type'] = "CrossAverage"
    robot['id'] = robot['_id']['$oid']
    robot['owner'] = robot['owner']['$oid']
    robot.pop("_cls")
    robot.pop("_id")
    return robot


def IFR2FromSchema(robotSchema):
    robot = IFR2(robotSchema.apiKey,
                 robotSchema.secret,
                 robotSchema.nickName,
                 robotSchema.symbol,
                 robotSchema.timeframe,
                 robotSchema.quantity,
                 robotSchema.intervalBegin,
                 robotSchema.intervalEnd,
                 robotSchema.periodIFR,
                 robotSchema.upper,
                 robotSchema.lower,
                 robotSchema.periodMean)
    return robot
