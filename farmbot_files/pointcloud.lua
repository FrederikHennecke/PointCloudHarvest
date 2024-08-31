-- settings
x_offset = 0
y_offset = 0
z_offset = 200
edges = 6
radius = 150
path = "./"
uart_path = "ttyS0"
plant_group_id = 97689

-- generate polygon coordinates for circling plant
function generate_polygon(num_edges, radius)
    points = {}
    if(num_edges<=1) then
        points[1] = {}
        points[1][0] = 0
        points[1][1] = 0
        points[2] = {}
        points[2][0] = 0
        points[2][1] = 0
        return points
    end
    for i = 1, num_edges+1, 1 do
        angle = 2 * math.pi * i / num_edges
        x = radius * math.sin(angle)
        y = radius * math.cos(angle)
        points[i] = {}
        points[i][0] = x
        points[i][1] = y
    end
    points[num_edges+1] = points[1]
    return points
end

-- send uart message and wait for answer
function send_and_wait(message, this_uart)
    uart_write_error = this_uart.write(string.format("%s \n", message))
    if uart_write_error then
        toast(inspect(uart_write_error), "error")
        -- Handle errors etc..
    end

    -- Wait 60s for data...
    read_string, uart_read_error = this_uart.read(15000)
    if uart_read_error then
        toast(inspect(uart_read_error), "error")
    else
        toast(inspect(read_string))
    end
end


-- main function
function main()
    -- device name, baud rate:
    my_uart, error = uart.open(uart_path, 9600)
    if error then
        toast(inspect(error), "error")
        return
    end
    if my_uart then
        group_members = group(plant_group_id)
        for i,member in ipairs(group_members) do
            plant = api({
                method = "get",
                url = "/api/points/" .. member
            })
            move_absolute({
                x = plant.x,
                y = plant.y,
                z = 100,
                speed = 80})
            time_string = string.format("%04d%02d%02d%02d%02d%2d",
                    local_time("year"),
                    local_time("month"),
                    local_time("day"),
                    local_time("hour"),
                    local_time("minute"),
                    local_time("second"))
            file_name = string.format("%s_%s", member, time_string)
            uart_write_error = my_uart.write(string.format("f_%s \n", file_name))
            wait(3000)
            if uart_write_error then
                toast(inspect(uart_write_error), "error sending data")
                return
            end
            points = generate_polygon(edges, radius)
            for i = 1,edges+1 do
                move_absolute({
                    x = math.floor(points[i][0])+plant.x,
                    y = math.floor(points[i][1])+plant.y,
                    z = 100,
                    speed = 25})
            end
            if(edges == 1) then
                wait(5000)
            end
            send_and_wait("stop", my_uart)
        end
        my_uart.close()
    end
end

main()