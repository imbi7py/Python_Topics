# _____ _3
#
# sqlite_file _ 'my_first_db.sqlite'    # name of the sqlite database file
# table_name _ 'my_table_2'   # name of the table to be created
# id_column _ 'my_1st_column' # name of the PRIMARY KEY column
# new_column1 _ 'my_2nd_column'  # name of the new column
# new_column2 _ 'my_3nd_column'  # name of the new column
# column_type _ 'TEXT' # E.g., INTEGER, TEXT, NULL, REAL, BLOB
# default_val _ 'Hello World' # a default value for the new column rows
#
# # Connecting to the database file
# conn _ _3.co.. s_f..
# c _ ?.cu..
#
# # A) Adding a new column without a row value
# ?.ex..("ALTER TABLE @ ADD COLUMN '@' @"\
#         .f..(tn_? cn_? ct_?
#
# # B) Adding a new column with a default row value
# ?.ex..("ALTER TABLE @ ADD COLUMN '@' @ DEFAULT '@'"\
#         .f..(tn_? cn_? ct_? df_?
#
# # Committing changes and closing the connection to the database file
# ?.co..
# ?.cl..
