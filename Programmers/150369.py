def solution(cap, n, deliveries, pickups):
    distance = 0

    while deliveries or pickups:
        disMax = 0
        d_tmp = 0
        p_tmp = 0

        while deliveries:
            d = deliveries.pop()
            if d == 0:
                continue
            elif d_tmp + d >= cap:
                disMax = max(disMax, len(deliveries)+1)
                deliveries.append(d_tmp + d - cap)
                break
            else:
                d_tmp += d
                disMax = max(disMax, len(deliveries)+1)
                continue

        while pickups:
            p = pickups.pop()
            if p == 0:
                continue
            elif p_tmp + p >= cap:
                disMax = max(disMax, len(pickups)+1)
                pickups.append(p_tmp + p - cap)
                break
            else:
                p_tmp += p
                disMax = max(disMax, len(pickups)+1)
                continue

        distance += (disMax * 2)

    return distance
