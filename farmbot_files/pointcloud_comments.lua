-- settings
-- x camera offset
x_offset = 0
-- y camera offset
y_offset = 0
-- z camera offset
z_offset = 100
-- number of edges for polygon for circling plant (must be at least 1)
edges = 6
-- radius for circling plant
radius = 150
-- folder path for saving the recordings
path = "./"
-- uart file path
uart_path = "ttyS0"
-- plant group id of all the plants to record
plant_group_id = 97689

--- generate polygon coordinates for circling plant
--- @param num_edges number of edges to create polygon from
--- @param radius number for the polygon
--- @return table list a list of points , which represents the n-edges polygon
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

--- send uart message and wait for answer
--- creates a list of points, which represents the n-edges polygon
--- @param message string edges to create polygon from
--- @param this_uart uart the polygon
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


--- main function
function main()
    -- connect to uart device: name, baud rate:
    my_uart, error = uart.open(uart_path, 9600)
    if error then
        toast(inspect(error), "error")
        return
    end
    -- if connection successful
    if my_uart then
        -- get all plants
        group_members = group(plant_group_id)
        for i,member in ipairs(group_members) do
            -- get coordinates of next plant
            plant = api({
                method = "get",
                url = "/api/points/" .. member
            })
            -- move to plant
            move_absolute({
                x = plant.x,
                y = plant.y,
                z = z_offset,
                speed = 80})
            -- get timestring for file name
            time_string = string.format("%04d%02d%02d%02d%02d%2d",
                    local_time("year"),
                    local_time("month"),
                    local_time("day"),
                    local_time("hour"),
                    local_time("minute"),
                    local_time("second"))
            file_name = string.format("%s_%s", member, time_string)
            -- start recording (pass timestring and plant id for folder name)
            uart_write_error = my_uart.write(string.format("f_%s \n", file_name))
            -- wait 3s for recording to start (usually takes 1-2 seconds)
            wait(3000)
            -- stop if it is not possible to write message
            if uart_write_error then
                toast(inspect(uart_write_error), "error sending data")
                return
            end
            -- get list of points for polygon
            points = generate_polygon(edges, radius)
            -- circle plant
            for j = 1,edges+1 do
                move_absolute({
                    x = math.floor(points[j][0])+plant.x,
                    y = math.floor(points[j][1])+plant.y,
                    z = z_offset,
                    speed = 25})
            end
            -- take multiple images for a single points (less noise)
            if(edges == 1) then
                wait(5000)
            end
            -- end recording
            send_and_wait("stop", my_uart)
        end
        -- close connection
        my_uart.close()
    end
end

main()