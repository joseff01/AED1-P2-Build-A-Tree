import pygame


class Node:
    def __init__(self, node_type, number):
        self.type = node_type
        self.number = number
        self.receiver = 0
