#! /usr/bin/env python
# -*- coding: utf-8 -*-

"""Tri par séléction.

Complexité en moyenne : O(n^2)
Complexité maximale : O(n^2)

"""


def selection(tab):
    taille = len(tab)

    for position in range(taille - 1):
        indice_min = min_indice_tableau(position, tab)
        echange(indice_min, position, tab)


def min_indice_tableau(indice_depart, tableau):
    indice_min = indice_depart
    for position in range(indice_depart, len(tableau)):
        if tableau[position] < tableau[indice_min]:
            indice_min = position

    return indice_min


def echange(i, j, tableau):
    tableau[i], tableau[j] = tableau[j], tableau[i]

def test_min_indice_tableau():
    tab = [1, 3, 2, 6, 4, 5]
    
    assert 0 == min_indice_tableau(0, tab)
    assert 4 == min_indice_tableau(3, tab)
    assert 5 == min_indice_tableau(5, tab)
    assert 2 == min_indice_tableau(1, tab)

def test_echange():
    tab = [1, 2, 3]
    echange(0, 2, tab)
    
    assert [3, 2, 1] == tab

def test_unique_element():
    tab = [1]
    
    selection(tab)
    assert [1] == tab
    
    
def test_deja_trie():
    tab = list(range(20))
    
    selection(tab)
    assert list(range(20)) == tab
    
def test_trie_a_l_envers():
    tab = list(range(20))
    tab.reverse()
    
    selection(tab)
    assert list(range(20)) == tab
    
def test_trie():
    tab = [1, 3, 2, 6, 4, 5]
    tab.reverse()
    
    selection(tab)
    assert [1, 2, 3, 4, 5, 6] == tab