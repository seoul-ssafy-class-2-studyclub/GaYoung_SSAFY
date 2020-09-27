t1 = [[1,2],[3,4],[5,6],[-1,7],[8,9],[-1,-1],[-1,-1],[-1,-1],[-1,-1],[-1,-1]]
t2 = [[1,2],[-1,-1],[-1,-1]]

# t1 = [[1,2],[3,4],[5,6],[-1,7],[8,9],[-1,-1],[-1,-1],[-1,-1],[-1,-1],[-1,-1]]
# t2 = [[-1, 1], [-1, -1]]

# SELECT A.ID, A.NAME, COUNT(*) FROM PLACES A LEFT OUTER JOIN PLACE_REVIEWS B ON A.ID = B.PLACE_ID GROUP BY B.PLACE_ID ORDER BY A.ID ASC;