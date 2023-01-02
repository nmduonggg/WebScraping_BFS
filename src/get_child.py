from bs4 import BeautifulSoup
from Node import Node
import time
import requests
import socket
from urllib3.connection import HTTPConnection

HTTPConnection.default_socket_options = (
    HTTPConnection.default_socket_options + [
        (socket.SOL_SOCKET, socket.SO_KEEPALIVE, 1),
        (socket.SOL_TCP, socket.TCP_KEEPIDLE, 45),
        (socket.SOL_TCP, socket.TCP_KEEPINTVL, 10),
        (socket.SOL_TCP, socket.TCP_KEEPCNT, 6)
    ]
)


def get_child_properites(rel_url):
    '''
    Input: Parent link
    Output: All possible children nodes including moves, values, links
            (move, value, link)
    '''
    
    url = "https://www.crazy-sensei.com" + rel_url
    headers = {
        "User-Agent": "Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/71.1.2222.33 Safari/537.36",
        "Accept-Encoding": "*",
        "Connection": "keep-alive",
        'Content-Type': 'application/json',
        'accept': 'application/json'
    }

    time.sleep(0.008)
    session = requests.Session()
    source = session.get(url, headers = headers)
    soup = BeautifulSoup(source.text, 'lxml')

    nodes = []

    table_body = soup.find('table')
    rows = table_body.find_all('tr')
    
    for row in rows[1:]:  # Remove header
        temp_cols = row.find_all('td')
        cols = []
        row_link = 0

        for x in temp_cols:
            cols.append(x.text.strip())
            link = x.find('a', href = True)
            if link != None:
                row_link = link['href']
        
        # End
        if len(cols) == 1: nodes.append(('**', cols[0], '**'))
        else: nodes.append((cols[1], cols[2], row_link)) # Get move, value, link
    
    source.close()
    return nodes



def get_child_nodes(parent_node):
    p_link = parent_node.link
    p_move = parent_node.move

    if p_link == '**':
        return []

    else:
        nodes = []
        for c in get_child_properites(p_link):
            c_move, c_value, c_link = c
            c_node = Node(p_move + "_" + c_move, c_value, c_link)
            nodes.append(c_node)
        return nodes
