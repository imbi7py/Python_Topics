# ______ n.. __ np
#
# MOD _ 666013
#
# ___ run_classic_dp n m
#     dp _ __.z.. ?2+1, ?1, ?1))
#     ?[0, 0, 0] _ 1
#     ___ k __ ra..(1, ?2+1):
#         ___ i __ ra..(?1):
#             ___ j __ ra.. ?1
#                 n1 _ ?|?-1, ?-1, ? __ ?2-1 >_ 0 ____ 0
#                 n2 _ ?|?-1, ?, ?-1 __ ?3-1 >_ 0 ____ 0
#                 n3 _ ?|?-1, ?+1, ? __ ?+1 < ?1 ____ 0
#                 n4 _ ?|?-1, ?, ?+1 __ ?3+1 < ?1 ____ 0
#                 ?|? ? ? _ ? + ? + ? + ?
#                 ?|? ? ? %_ M..
#     r_ ?|?2, ?1-1, ?1-1
#
#
# ___ run_new_dp n m
#     log2m _ in. __.__2 ?2
#     dp _ __.z.. __2_+1, ?1 ?1 ?1 ?1
#     ___ i __ ra.. ?1
#         ___ j __ ra.. ?1
#             __ i + 1 < ?1
#                 ?|0 ? ? ?1 + 1 ?2| _ 1
#             __ ?1 - 1 >_ 0
#                 ?|0, ? ? ?1 - 1 ?2| _ 1
#             __ ?2 + 1 < ?1
#                 ?|0 ?1 ?2 ?1 ?2 + 1| _ 1
#             __ ?2 - 1 >_ 0:
#                 ?|0 ? ? ?1 ?2 - 1| _ 1
#
#     ___ k __ ra.. 1 __2_ + 1
#         ___ i1 __ ra.. ?1
#             ___ j1 __ ra.. ?1
#                 ___ i2 __ ra.. ?1
#                     ___ j2 __ ra.. ?1
#                         ___ p __ ra.. ?1
#                             ___ q __ ra.. ?1
#                                 ?|? ? ? ? ? +_ ?|?1-1 ?2, ?3 p q| *\
#                                                          ?|?1-1 p q i2 j2
#                                 ?[k, i1, j1, i2, j2] %_ M..
#
#     __ 2 ** __2_ __ ?2
#         r_ ?|__2_ 0 0 ?1 - 1, ?1 - 1
#     binary _ '{0:b}'.f.. ?2 |;;-1
#     results _ N..
#     ___ i b __ en..  b..
#         __ b __ '1' an. r.. __ N..
#             r.. _ ?|? 0 0 : :
#         ____ b __ '1'
#             new_results _ __.z_l.. r..
#             ___ k1 __ ra.. ?1
#                 ___ k2 __ ra.. ?1
#                     ___ p __ ra.. ?1
#                         ___ q __ ra.. ?1
#                             n..__1 _2 +_ r..|? ? *\
#                                                    ?|i, p q k1 k2
#                             n..|_1 _2 %_ M..
#             r.. _ n..
#     r_ ?|?1 - 1 ?1 - 1
#
# print(r_c_d.. 6, 100
# print(r_n_d.. 6, 100
# print(r_n_d.(5, 10 ** 18))
#
# ___ ?1 __ ra.. 2  5
#     ___ ?2 __ ra.. 2 100
#         classic _ r_c_d0 ?1 ?2
#         new _ r_n_d. ?1 ?2
#         as.. cl.. __ n.. 'classic_@, new_@, n_@, m_@'.f..(
#             c..
#             n..0
#             ?1
#             m
#         )