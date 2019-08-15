#include <iostream>
#include <cstdio>
#include <cstring>
#include <cstdlib>

using namespace std;

int main(int argc, char **argv)
{
    int test_case;
    int T;
    /*
	   아래의 freopen 함수는 input.txt 를 read only 형식으로 연 후,
	   앞으로 표준 입력(키보드) 대신 input.txt 파일로부터 읽어오겠다는 의미의 코드입니다.
	   //여러분이 작성한 코드를 테스트 할 때, 편의를 위해서 input.txt에 입력을 저장한 후,
	   freopen 함수를 이용하면 이후 cin 을 수행할 때 표준 입력 대신 파일로부터 입력을 받아올 수 있습니다.
	   따라서 테스트를 수행할 때에는 아래 주석을 지우고 이 함수를 사용하셔도 좋습니다.
	   freopen 함수를 사용하기 위해서는 #include <cstdio>, 혹은 #include <stdio.h> 가 필요합니다.
	   단, 채점을 위해 코드를 제출하실 때에는 반드시 freopen 함수를 지우거나 주석 처리 하셔야 합니다.
	*/
    freopen("input.txt", "r", stdin);
    cin >> T;
    /*
	   여러 개의 테스트 케이스가 주어지므로, 각각을 처리합니다.
	*/
    for (test_case = 1; test_case <= T; ++test_case)
    {
        char current_time[256];
        char plan_time[256];
        char *current_hour;
        char *current_minute;
        char *current_second;
        char *plan_hour;
        char *plan_minute;
        char *plan_second;

        cin >> current_time >> plan_time;
        current_hour = strtok(current_time, ":");
        current_minute = strtok(NULL, ":");
        current_second = strtok(NULL, ":");
        plan_hour = strtok(plan_time, ":");
        plan_minute = strtok(NULL, ":");
        plan_second = strtok(NULL, ":");
        int current = atoi(current_hour) * 60 * 60 + atoi(current_minute) * 60 + atoi(current_second);
        int plan = atoi(plan_hour) * 60 * 60 + atoi(plan_minute) * 60 + atoi(plan_second);
        if (current > plan)
        {
            plan += 24 * 60 * 60;
        }

        int remain = plan - current;
        int remain_hour = remain / (60 * 60);
        int remain_minute = (remain % (60 * 60)) / 60;
        int remain_second = (remain % (60 * 60)) % 60;

        cout.fill('0');

        cout << "#" << test_case;
        cout << " ";
        cout.width(2);
        cout << remain_hour;
        cout << ":";
        cout.width(2);
        cout << remain_minute;
        cout << ":";
        cout.width(2);
        cout << remain_second << endl;
    }
    return 0; //정상종료시 반드시 0을 리턴해야합니다.
}