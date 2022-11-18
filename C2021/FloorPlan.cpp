/**************************************************************
*                                                                         *
* 문제 : 방의 크기 구하기                                        *
*                                                                        *
***************************************************************/

#include <iostream>
#include <string>
using namespace std;

void searchFloorPlan();
int  searchRoom(int y, int x, int count);
void bubbleSort(int *data, int size);

int main(void)
{
        searchFloorPlan();
}

#define MAX_SIZE (100+1)
#define MAX_ROOMS 100

#define EMPTY    -1
#define WALL     -2

int     floorPlan[MAX_SIZE][MAX_SIZE];

/* 평면도에서 각 방의 크기를 구하는 함수 */
void searchFloorPlan()
{
    int  i, j;
    int  width, height;
    int  roomCount;
    int  roomSize[MAX_ROOMS];

    cin >> width >> height;

    for (i=0; i<height; i++)
    {
        char line[MAX_SIZE];

        cin >> line;

        for(j=0; line[j]; j++)
            if (line[j] == '+')
                floorPlan[i][j] = WALL;
            else
                floorPlan[i][j] = EMPTY;
    }

    roomCount = 0;
    for (i=0; i<height; i++)
        for (j=0; j<width; j++)
        {
            if (floorPlan[i][j] == EMPTY)
            {
                roomSize[roomCount] = searchRoom(i, j, roomCount);
                roomCount++;
            }
        }

    bubbleSort(roomSize, roomCount);

    cout << roomCount << endl;
    for(i=0; i<roomCount; i++)
        cout << roomSize[i] << ' ';
    cout << endl;
}

/*
 * 현재 방의 일부인 위치 (x, y)에서 주위를 되부름으로 검색하면서
 * 전체 방의 크기를 계산하는 함수
 */
int searchRoom(int y, int x, int count)
{
    int left, right, up, down;

    if (floorPlan[y][x] != EMPTY)
        return 0;

    floorPlan[y][x] = count;

    left  = searchRoom(y,   x-1, count);
    right = searchRoom(y,   x+1, count);
    up    = searchRoom(y+1, x,   count);
    down  = searchRoom(y-1, x,   count);

    return left + right + up + down + 1;
}

/* 방의 크기순으로 정렬하는 버블 정렬 함수 */
void bubbleSort(int *data, int size)
{
    int i, j;

    for(i=0; i<size-1; i++)
        for(j=0; j<size-1-i; j++)
        {
            if (data[j+1] > data[j])
            {
                int tmp;

                tmp = data[j];
                data[j] = data[j+1];
                data[j+1] = tmp;
            }
        }
}

