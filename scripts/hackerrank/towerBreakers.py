
# see: https://www.hackerrank.com/challenges/one-month-preparation-kit-tower-breakers-1/forum?isFullScreen=true&h_l=interview&playlist_slugs%5B%5D=preparation-kits&playlist_slugs%5B%5D=one-month-preparation-kit&playlist_slugs%5B%5D=one-month-week-two

"""
The simple explanation to this is if number of towers is even P2 can always mirror the moves done by P1 and if number of towers are odd P1 reduces one of the towers to 1 and then uses exact same mirroring strategy to beat P2. Unless ofcourse if all towers all aready of size 1 then P1 loses.
"""

def towerBreakers(n, m):
    if n%2==0 or m==1:
        return 2
    else:
        return 1
    
if __name__ == "__main__":
    print(towerBreakers(2, 2))
    # expected = 2