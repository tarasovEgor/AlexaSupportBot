
async def calculate_plan_price(infrastructure_data: dict) -> float:
    PC_price = await get_PC_price(int(infrastructure_data['PC_count']))
    server_price = await get_server_price(int(infrastructure_data['server_count']))
    program_price = await get_program_price(int(infrastructure_data['program_type']))
    return float(PC_price + server_price + program_price)


async def get_PC_price(PC_count: int):
    match PC_count:
        case 1:
            return 1200
        case _ if PC_count > 1 and PC_count <= 5:
            return 1200
        case _ if PC_count > 5 and PC_count < 10:
            return 1000
        case _ if PC_count >= 10 and PC_count < 50:
            return 900
        case _ if PC_count >= 50:
            return 700


async def get_server_price(server_count: int):
    match server_count:
        case 1:
            return 2500
        case 2:
            return 2500
        case _ if server_count > 2 and server_count < 5:
            return 2000
        case _ if server_count >= 5 and server_count < 10:
            return 1500
        case _ if server_count >= 10:
            return 1000
        

async def get_program_price(program_type: int):
    match program_type:
        case 1:
            return 0
        case 2:
            return 12000
        case 3:
            return 25000