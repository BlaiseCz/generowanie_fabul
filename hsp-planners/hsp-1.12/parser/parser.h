/* A Bison parser, made by GNU Bison 2.3.  */

/* Skeleton interface for Bison's Yacc-like parsers in C

   Copyright (C) 1984, 1989, 1990, 2000, 2001, 2002, 2003, 2004, 2005, 2006
   Free Software Foundation, Inc.

   This program is free software; you can redistribute it and/or modify
   it under the terms of the GNU General Public License as published by
   the Free Software Foundation; either version 2, or (at your option)
   any later version.

   This program is distributed in the hope that it will be useful,
   but WITHOUT ANY WARRANTY; without even the implied warranty of
   MERCHANTABILITY or FITNESS FOR A PARTICULAR PURPOSE.  See the
   GNU General Public License for more details.

   You should have received a copy of the GNU General Public License
   along with this program; if not, write to the Free Software
   Foundation, Inc., 51 Franklin Street, Fifth Floor,
   Boston, MA 02110-1301, USA.  */

/* As a special exception, you may create a larger work that contains
   part or all of the Bison parser skeleton and distribute that work
   under terms of your choice, so long as that work isn't itself a
   parser generator using the skeleton or a modified version thereof
   as a parser skeleton.  Alternatively, if you modify or redistribute
   the parser skeleton itself, you may (at your option) remove this
   special exception, which will cause the skeleton and the resulting
   Bison output files to be licensed under the GNU General Public
   License without this special exception.

   This special exception was added by the Free Software Foundation in
   version 2.2 of Bison.  */

/* Tokens.  */
#ifndef YYTOKENTYPE
# define YYTOKENTYPE
   /* Put the tokens into the symbol table, so that GDB and other debuggers
      know about them.  */
   enum yytokentype {
     LEFTPAR = 258,
     RIGHTPAR = 259,
     NAME = 260,
     TWODOTS = 261,
     DEFINE = 262,
     DOMAIN = 263,
     REQUIREMENTS = 264,
     CONSTANTS = 265,
     PREDICATES = 266,
     QUESTION = 267,
     STRIPS = 268,
     EQUALITY = 269,
     CONDITIONAL = 270,
     DOM_AXIOMS = 271,
     DISJUNCTIVE = 272,
     ADL = 273,
     E_PRECONDITIONS = 274,
     U_PRECONDITIONS = 275,
     AND = 276,
     NOT = 277,
     FORALL = 278,
     WHEN = 279,
     EQUAL = 280,
     ACTION = 281,
     PARAMETERS = 282,
     PRECONDITION = 283,
     EFFECT = 284,
     PROBLEM = 285,
     INIT = 286,
     GOAL = 287,
     LENGTH = 288,
     SITUATION = 289,
     OBJECTS = 290,
     SERIAL = 291,
     PARALLEL = 292,
     INTEGER = 293,
     TYPING = 294,
     TYPES = 295
   };
#endif
/* Tokens.  */
#define LEFTPAR 258
#define RIGHTPAR 259
#define NAME 260
#define TWODOTS 261
#define DEFINE 262
#define DOMAIN 263
#define REQUIREMENTS 264
#define CONSTANTS 265
#define PREDICATES 266
#define QUESTION 267
#define STRIPS 268
#define EQUALITY 269
#define CONDITIONAL 270
#define DOM_AXIOMS 271
#define DISJUNCTIVE 272
#define ADL 273
#define E_PRECONDITIONS 274
#define U_PRECONDITIONS 275
#define AND 276
#define NOT 277
#define FORALL 278
#define WHEN 279
#define EQUAL 280
#define ACTION 281
#define PARAMETERS 282
#define PRECONDITION 283
#define EFFECT 284
#define PROBLEM 285
#define INIT 286
#define GOAL 287
#define LENGTH 288
#define SITUATION 289
#define OBJECTS 290
#define SERIAL 291
#define PARALLEL 292
#define INTEGER 293
#define TYPING 294
#define TYPES 295




#if ! defined YYSTYPE && ! defined YYSTYPE_IS_DECLARED
typedef int YYSTYPE;
# define yystype YYSTYPE /* obsolescent; will be withdrawn */
# define YYSTYPE_IS_DECLARED 1
# define YYSTYPE_IS_TRIVIAL 1
#endif

extern YYSTYPE yylval;

