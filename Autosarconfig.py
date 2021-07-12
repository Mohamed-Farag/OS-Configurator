/*
 * AutoSARConfig.c
 *
 *  Created on: Mar 29, 2018
 *      Author: Dell
 */


#include "AutoSARConfig.h"


UBaseType_t const volatile Null;
OsResource GlobalRes;


#ifndef TASK_1_RESOURCE_1
    #define TASK_1_RESOURCE_1       Null
#endif
#ifndef TASK_1_RESOURCE_2
    #define TASK_1_RESOURCE_2       Null
#endif
#ifndef TASK_1_RESOURCE_3
    #define TASK_1_RESOURCE_3       Null
#endif
#ifndef TASK_1_RESOURCE_4
    #define TASK_1_RESOURCE_4       Null
#endif
#ifndef TASK_1_RESOURCE_5
    #define TASK_1_RESOURCE_5       Null
#endif
#ifndef TASK_1_RESOURCE_6
    #define TASK_1_RESOURCE_6       Null
#endif
#ifndef TASK_1_RESOURCE_7
    #define TASK_1_RESOURCE_7       Null
#endif
#ifndef TASK_1_RESOURCE_8
    #define TASK_1_RESOURCE_8       Null
#endif

#ifndef TASK_2_RESOURCE_1
    #define TASK_2_RESOURCE_1       Null
#endif
#ifndef TASK_2_RESOURCE_2
    #define TASK_2_RESOURCE_2       Null
#endif
#ifndef TASK_2_RESOURCE_3
    #define TASK_2_RESOURCE_3       Null
#endif
#ifndef TASK_2_RESOURCE_4
    #define TASK_2_RESOURCE_4       Null
#endif
#ifndef TASK_2_RESOURCE_5
    #define TASK_2_RESOURCE_5       Null
#endif
#ifndef TASK_2_RESOURCE_6
    #define TASK_2_RESOURCE_6       Null
#endif
#ifndef TASK_2_RESOURCE_7
    #define TASK_2_RESOURCE_7       Null
#endif
#ifndef TASK_2_RESOURCE_8
    #define TASK_2_RESOURCE_8       Null
#endif

#ifndef TASK_3_RESOURCE_1
    #define TASK_3_RESOURCE_1       Null
#endif
#ifndef TASK_3_RESOURCE_2
    #define TASK_3_RESOURCE_2       Null
#endif
#ifndef TASK_3_RESOURCE_3
    #define TASK_3_RESOURCE_3       Null
#endif
#ifndef TASK_3_RESOURCE_4
    #define TASK_3_RESOURCE_4       Null
#endif
#ifndef TASK_3_RESOURCE_5
    #define TASK_3_RESOURCE_5       Null
#endif
#ifndef TASK_3_RESOURCE_6
    #define TASK_3_RESOURCE_6       Null
#endif
#ifndef TASK_3_RESOURCE_7
    #define TASK_3_RESOURCE_7       Null
#endif
#ifndef TASK_3_RESOURCE_8
    #define TASK_3_RESOURCE_8       Null
#endif

#ifndef TASK_4_RESOURCE_1
    #define TASK_4_RESOURCE_1       Null
#endif
#ifndef TASK_4_RESOURCE_2
    #define TASK_4_RESOURCE_2       Null
#endif
#ifndef TASK_4_RESOURCE_3
    #define TASK_4_RESOURCE_3       Null
#endif
#ifndef TASK_4_RESOURCE_4
    #define TASK_4_RESOURCE_4       Null
#endif
#ifndef TASK_4_RESOURCE_5
    #define TASK_4_RESOURCE_5       Null
#endif
#ifndef TASK_4_RESOURCE_6
    #define TASK_4_RESOURCE_6       Null
#endif
#ifndef TASK_4_RESOURCE_7
    #define TASK_4_RESOURCE_7       Null
#endif
#ifndef TASK_4_RESOURCE_8
    #define TASK_4_RESOURCE_8       Null
#endif

#ifndef TASK_5_RESOURCE_1
    #define TASK_5_RESOURCE_1       Null
#endif
#ifndef TASK_5_RESOURCE_2
    #define TASK_5_RESOURCE_2       Null
#endif
#ifndef TASK_5_RESOURCE_3
    #define TASK_5_RESOURCE_3       Null
#endif
#ifndef TASK_5_RESOURCE_4
    #define TASK_5_RESOURCE_4       Null
#endif
#ifndef TASK_5_RESOURCE_5
    #define TASK_5_RESOURCE_5       Null
#endif
#ifndef TASK_5_RESOURCE_6
    #define TASK_5_RESOURCE_6       Null
#endif
#ifndef TASK_5_RESOURCE_7
    #define TASK_5_RESOURCE_7       Null
#endif
#ifndef TASK_5_RESOURCE_8
    #define TASK_5_RESOURCE_8       Null
#endif

#ifndef TASK_6_RESOURCE_1
    #define TASK_6_RESOURCE_1       Null
#endif
#ifndef TASK_6_RESOURCE_2
    #define TASK_6_RESOURCE_2       Null
#endif
#ifndef TASK_6_RESOURCE_3
    #define TASK_6_RESOURCE_3       Null
#endif
#ifndef TASK_6_RESOURCE_4
    #define TASK_6_RESOURCE_4       Null
#endif
#ifndef TASK_6_RESOURCE_5
    #define TASK_6_RESOURCE_5       Null
#endif
#ifndef TASK_6_RESOURCE_6
    #define TASK_6_RESOURCE_6       Null
#endif
#ifndef TASK_6_RESOURCE_7
    #define TASK_6_RESOURCE_7       Null
#endif
#ifndef TASK_6_RESOURCE_8
    #define TASK_6_RESOURCE_8       Null
#endif

/* these macros function to declare only specific number of resources
 * in task not declare 8 resources for all tasks */

#define _8_RESOURCES_IN_TASK(ExtTaskID)                                                                      \
        OsResource * ResourcesInTask_##ExtTaskID[8] = {\
                                                       (OsResource *) &TASK_## ExtTaskID ##_RESOURCE_1,      \
                                                       (OsResource *) &TASK_## ExtTaskID ##_RESOURCE_2,      \
                                                       (OsResource *) &TASK_## ExtTaskID ##_RESOURCE_3,      \
                                                       (OsResource *) &TASK_## ExtTaskID ##_RESOURCE_4,      \
                                                       (OsResource *) &TASK_## ExtTaskID ##_RESOURCE_5,      \
                                                       (OsResource *) &TASK_## ExtTaskID ##_RESOURCE_6,      \
                                                       (OsResource *) &TASK_## ExtTaskID ##_RESOURCE_7,      \
                                                       (OsResource *) &TASK_## ExtTaskID ##_RESOURCE_8};

#define _7_RESOURCES_IN_TASK(ExtTaskID)                                                                      \
        OsResource * ResourcesInTask_##ExtTaskID[7] = {\
                                                       (OsResource *) &TASK_## ExtTaskID ##_RESOURCE_1,      \
                                                       (OsResource *) &TASK_## ExtTaskID ##_RESOURCE_2,      \
                                                       (OsResource *) &TASK_## ExtTaskID ##_RESOURCE_3,      \
                                                       (OsResource *) &TASK_## ExtTaskID ##_RESOURCE_4,      \
                                                       (OsResource *) &TASK_## ExtTaskID ##_RESOURCE_5,      \
                                                       (OsResource *) &TASK_## ExtTaskID ##_RESOURCE_6,      \
                                                       (OsResource *) &TASK_## ExtTaskID ##_RESOURCE_7};
#define _6_RESOURCES_IN_TASK(ExtTaskID)                                                                      \
        OsResource * ResourcesInTask_##ExtTaskID[6] = {\
                                                       (OsResource *) &TASK_## ExtTaskID ##_RESOURCE_1,      \
                                                       (OsResource *) &TASK_## ExtTaskID ##_RESOURCE_2,      \
                                                       (OsResource *) &TASK_## ExtTaskID ##_RESOURCE_3,      \
                                                       (OsResource *) &TASK_## ExtTaskID ##_RESOURCE_4,      \
                                                       (OsResource *) &TASK_## ExtTaskID ##_RESOURCE_5,      \
                                                       (OsResource *) &TASK_## ExtTaskID ##_RESOURCE_6};
#define _5_RESOURCES_IN_TASK(ExtTaskID)                                                                      \
        OsResource * ResourcesInTask_##ExtTaskID[5] = {\
                                                       (OsResource *) &TASK_## ExtTaskID ##_RESOURCE_1,      \
                                                       (OsResource *) &TASK_## ExtTaskID ##_RESOURCE_2,      \
                                                       (OsResource *) &TASK_## ExtTaskID ##_RESOURCE_3,      \
                                                       (OsResource *) &TASK_## ExtTaskID ##_RESOURCE_4,      \
                                                       (OsResource *) &TASK_## ExtTaskID ##_RESOURCE_5};
#define _4_RESOURCES_IN_TASK(ExtTaskID)                                                                      \
        OsResource * ResourcesInTask_##ExtTaskID[4] = {\
                                                       (OsResource *) &TASK_## ExtTaskID ##_RESOURCE_1,      \
                                                       (OsResource *) &TASK_## ExtTaskID ##_RESOURCE_2,      \
                                                       (OsResource *) &TASK_## ExtTaskID ##_RESOURCE_3,      \
                                                       (OsResource *) &TASK_## ExtTaskID ##_RESOURCE_4};
#define _3_RESOURCES_IN_TASK(ExtTaskID)                                                                      \
        OsResource * ResourcesInTask_##ExtTaskID[3] = {\
                                                       (OsResource *) &TASK_## ExtTaskID ##_RESOURCE_1,      \
                                                       (OsResource *) &TASK_## ExtTaskID ##_RESOURCE_2,      \
                                                       (OsResource *) &TASK_## ExtTaskID ##_RESOURCE_3};
#define _2_RESOURCES_IN_TASK(ExtTaskID)                                                                      \
        OsResource * ResourcesInTask_##ExtTaskID[2] = {\
                                                       (OsResource *) &TASK_## ExtTaskID ##_RESOURCE_1,      \
                                                       (OsResource *) &TASK_## ExtTaskID ##_RESOURCE_2};
#define _1_RESOURCES_IN_TASK(ExtTaskID)                                                                      \
        OsResource * ResourcesInTask_##ExtTaskID[1] = {\
                                                       (OsResource *) &TASK_## ExtTaskID ##_RESOURCE_1};

#define _0_RESOURCES_IN_TASK(ExtTaskID)                                                                      \
        OsResource * ResourcesInTask_##ExtTaskID = (OsResource *) &GlobalRes;



#if NUMBER_OF_RESOURCES > 0

#ifndef RESOURCE_LINKEDRESOURCE_1
    #define RESOURCE_LINKEDRESOURCE_1   Null
#endif
#ifndef RESOURCE_LINKEDRESOURCE_2
    #define RESOURCE_LINKEDRESOURCE_2   Null
#endif
#ifndef RESOURCE_LINKEDRESOURCE_3
    #define RESOURCE_LINKEDRESOURCE_3   Null
#endif
#ifndef RESOURCE_LINKEDRESOURCE_4
    #define RESOURCE_LINKEDRESOURCE_4   Null
#endif
#ifndef RESOURCE_LINKEDRESOURCE_5
    #define RESOURCE_LINKEDRESOURCE_5   Null
#endif
#ifndef RESOURCE_LINKEDRESOURCE_6
    #define RESOURCE_LINKEDRESOURCE_6   Null
#endif
#ifndef RESOURCE_LINKEDRESOURCE_7
    #define RESOURCE_LINKEDRESOURCE_7   Null
#endif
#ifndef RESOURCE_LINKEDRESOURCE_8
    #define RESOURCE_LINKEDRESOURCE_8   Null
#endif
#ifndef RESOURCE_LINKEDRESOURCE_9
    #define RESOURCE_LINKEDRESOURCE_9   Null
#endif
#ifndef RESOURCE_LINKEDRESOURCE_10
    #define RESOURCE_LINKEDRESOURCE_10   Null
#endif
#ifndef RESOURCE_LINKEDRESOURCE_11
    #define RESOURCE_LINKEDRESOURCE_11   Null
#endif
#ifndef RESOURCE_LINKEDRESOURCE_12
    #define RESOURCE_LINKEDRESOURCE_12   Null
#endif
#ifndef RESOURCE_LINKEDRESOURCE_13
    #define RESOURCE_LINKEDRESOURCE_13   Null
#endif
#ifndef RESOURCE_LINKEDRESOURCE_14
    #define RESOURCE_LINKEDRESOURCE_14   Null
#endif
#ifndef RESOURCE_LINKEDRESOURCE_15
    #define RESOURCE_LINKEDRESOURCE_15   Null
#endif
#ifndef RESOURCE_LINKEDRESOURCE_16
    #define RESOURCE_LINKEDRESOURCE_16   Null
#endif
#ifndef RESOURCE_LINKEDRESOURCE_17
    #define RESOURCE_LINKEDRESOURCE_17   Null
#endif
#ifndef RESOURCE_LINKEDRESOURCE_18
    #define RESOURCE_LINKEDRESOURCE_18   Null
#endif
#ifndef RESOURCE_LINKEDRESOURCE_19
    #define RESOURCE_LINKEDRESOURCE_19   Null
#endif
#ifndef RESOURCE_LINKEDRESOURCE_20
    #define RESOURCE_LINKEDRESOURCE_20   Null
#endif

OsResource ResourceStruct[NUMBER_OF_RESOURCES];

/* Create Resource Handle (ID) for all Resources. The handle can be used to
GetResource, ReleaseResource.*/
UBaseType_t const RESOURCE_NAME_1 = (UBaseType_t) &ResourceStruct[0];
#if NUMBER_OF_RESOURCES >= 2
UBaseType_t const RESOURCE_NAME_2 = (UBaseType_t) &ResourceStruct[1];
#endif
#if NUMBER_OF_RESOURCES >= 3
UBaseType_t const volatile RESOURCE_NAME_3 = (UBaseType_t) &ResourceStruct[2];
#endif
#if NUMBER_OF_RESOURCES >= 4
UBaseType_t const volatile RESOURCE_NAME_4 = (UBaseType_t) &ResourceStruct[3];
#endif
#if NUMBER_OF_RESOURCES >= 5
UBaseType_t const volatile RESOURCE_NAME_5 = (UBaseType_t) &ResourceStruct[4];
#endif
#if NUMBER_OF_RESOURCES >= 6
UBaseType_t const volatile RESOURCE_NAME_6 = (UBaseType_t) &ResourceStruct[5];
#endif
#if NUMBER_OF_RESOURCES >= 7
UBaseType_t const volatile RESOURCE_NAME_7 = (UBaseType_t) &ResourceStruct[6];
#endif
#if NUMBER_OF_RESOURCES >= 8
UBaseType_t const volatile RESOURCE_NAME_8 = (UBaseType_t) &ResourceStruct[7];
#endif
#if NUMBER_OF_RESOURCES >= 9
UBaseType_t const volatile RESOURCE_NAME_9 = (UBaseType_t) &ResourceStruct[8];
#endif
#if NUMBER_OF_RESOURCES >= 10
UBaseType_t const volatile RESOURCE_NAME_10 = (UBaseType_t) &ResourceStruct[9];
#endif
#if NUMBER_OF_RESOURCES >= 11
UBaseType_t const volatile RESOURCE_NAME_11 = (UBaseType_t) &ResourceStruct[10];
#endif
#if NUMBER_OF_RESOURCES >= 12
UBaseType_t const volatile RESOURCE_NAME_12 = (UBaseType_t) &ResourceStruct[11];
#endif
#if NUMBER_OF_RESOURCES >= 13
UBaseType_t const volatile RESOURCE_NAME_13 = (UBaseType_t) &ResourceStruct[12];
#endif
#if NUMBER_OF_RESOURCES >= 14
UBaseType_t const volatile RESOURCE_NAME_14 = (UBaseType_t) &ResourceStruct[13];
#endif
#if NUMBER_OF_RESOURCES >= 15
UBaseType_t const volatile RESOURCE_NAME_15 = (UBaseType_t) &ResourceStruct[14];
#endif
#if NUMBER_OF_RESOURCES >= 16
UBaseType_t const volatile RESOURCE_NAME_16 = (UBaseType_t) &ResourceStruct[15];
#endif
#if NUMBER_OF_RESOURCES >= 17
UBaseType_t const volatile RESOURCE_NAME_17 = (UBaseType_t) &ResourceStruct[16];
#endif
#if NUMBER_OF_RESOURCES >= 18
UBaseType_t const volatile RESOURCE_NAME_18 = (UBaseType_t) &ResourceStruct[17];
#endif
#if NUMBER_OF_RESOURCES >= 19
UBaseType_t const volatile RESOURCE_NAME_19 = (UBaseType_t) &ResourceStruct[18];
#endif
#if NUMBER_OF_RESOURCES >= 20
UBaseType_t const volatile RESOURCE_NAME_20 = (UBaseType_t) &ResourceStruct[19];
#endif

/*************************** Resource struct ******************************************/

OsResource ResourceStruct[NUMBER_OF_RESOURCES] = {
                                                  {
                                                   .ResourceProperty = RESOURCE_PROPERTY_1,
                                                   .LinkedResource = (OsResourceContainer *) &RESOURCE_LINKEDRESOURCE_1,
                                                   .CeilingPriority = NULL,
                                                   .Availability = TRUE,
                                                  },
#if NUMBER_OF_RESOURCES >= 2
                                                  {
                                                   .ResourceProperty = RESOURCE_PROPERTY_2,
                                                   .LinkedResource = (OsResourceContainer *) &RESOURCE_LINKEDRESOURCE_2,
                                                   .CeilingPriority = NULL,
                                                   .Availability = TRUE,
                                                  },
#endif
#if NUMBER_OF_RESOURCES >= 3
                                                  {
                                                   .ResourceProperty = RESOURCE_PROPERTY_3,
                                                   .LinkedResource = (OsResourceContainer *) &RESOURCE_LINKEDRESOURCE_3,
                                                   .CeilingPriority = NULL,
                                                   .Availability = TRUE,
                                                  },
#endif
#if NUMBER_OF_RESOURCES >= 4
                                                  {
                                                   .ResourceProperty = RESOURCE_PROPERTY_4,
                                                   .LinkedResource = (OsResourceContainer *) &RESOURCE_LINKEDRESOURCE_4,
                                                   .CeilingPriority = NULL,
                                                   .Availability = TRUE,
                                                  },
#endif
#if NUMBER_OF_RESOURCES >= 5
                                                  {
                                                   .ResourceProperty = RESOURCE_PROPERTY_5,
                                                   .LinkedResource = (OsResourceContainer *) &RESOURCE_LINKEDRESOURCE_5,
                                                   .CeilingPriority = NULL,
                                                   .Availability = TRUE,
                                                  },
#endif
#if NUMBER_OF_RESOURCES >= 6
                                                  {
                                                   .ResourceProperty = RESOURCE_PROPERTY_6,
                                                   .LinkedResource = (OsResourceContainer *) &RESOURCE_LINKEDRESOURCE_6,
                                                   .CeilingPriority = NULL,
                                                   .Availability = TRUE,
                                                  },
#endif
#if NUMBER_OF_RESOURCES >= 7
                                                  {
                                                   .ResourceProperty = RESOURCE_PROPERTY_7,
                                                   .LinkedResource = (OsResourceContainer *) &RESOURCE_LINKEDRESOURCE_7,
                                                   .CeilingPriority = NULL,
                                                   .Availability = TRUE,
                                                  },
#endif
#if NUMBER_OF_RESOURCES >= 8
                                                  {
                                                   .ResourceProperty = RESOURCE_PROPERTY_8,
                                                   .LinkedResource = (OsResourceContainer *) &RESOURCE_LINKEDRESOURCE_8,
                                                   .CeilingPriority = NULL,
                                                   .Availability = TRUE,
                                                  },
#endif
#if NUMBER_OF_RESOURCES >= 9
                                                  {
                                                   .ResourceProperty = RESOURCE_PROPERTY_9,
                                                   .LinkedResource = (OsResourceContainer *) &RESOURCE_LINKEDRESOURCE_9,
                                                   .CeilingPriority = NULL,
                                                   .Availability = TRUE,
                                                  },
#endif
#if NUMBER_OF_RESOURCES >= 10
                                                  {
                                                   .ResourceProperty = RESOURCE_PROPERTY_10,
                                                   .LinkedResource = (OsResourceContainer *) &RESOURCE_LINKEDRESOURCE_10,
                                                   .CeilingPriority = NULL,
                                                   .Availability = TRUE,
                                                  },
#endif
#if NUMBER_OF_RESOURCES >= 11
                                                  {
                                                   .ResourceProperty = RESOURCE_PROPERTY_11,
                                                   .LinkedResource = (OsResourceContainer *) &RESOURCE_LINKEDRESOURCE_11,
                                                   .CeilingPriority = NULL,
                                                   .Availability = TRUE,
                                                  },
#endif
#if NUMBER_OF_RESOURCES >= 12
                                                  {
                                                   .ResourceProperty = RESOURCE_PROPERTY_12,
                                                   .LinkedResource = (OsResourceContainer *) &RESOURCE_LINKEDRESOURCE_12,
                                                   .CeilingPriority = NULL,
                                                   .Availability = TRUE,
                                                  },
#endif
#if NUMBER_OF_RESOURCES >= 13
                                                  {
                                                   .ResourceProperty = RESOURCE_PROPERTY_13,
                                                   .LinkedResource = (OsResourceContainer *) &RESOURCE_LINKEDRESOURCE_13,
                                                   .CeilingPriority = NULL,
                                                   .Availability = TRUE,
                                                  },
#endif
#if NUMBER_OF_RESOURCES >= 14
                                                  {
                                                   .ResourceProperty = RESOURCE_PROPERTY_14,
                                                   .LinkedResource = (OsResourceContainer *) &RESOURCE_LINKEDRESOURCE_14,
                                                   .CeilingPriority = NULL,
                                                   .Availability = TRUE,
                                                  },
#endif
#if NUMBER_OF_RESOURCES >= 15
                                                  {
                                                   .ResourceProperty = RESOURCE_PROPERTY_15,
                                                   .LinkedResource = (OsResourceContainer *) &RESOURCE_LINKEDRESOURCE_15,
                                                   .CeilingPriority = NULL,
                                                   .Availability = TRUE,
                                                  }
#endif
#if NUMBER_OF_RESOURCES >= 16
                                                  {
                                                   .ResourceProperty = RESOURCE_PROPERTY_16,
                                                   .LinkedResource = (OsResourceContainer *) &RESOURCE_LINKEDRESOURCE_16,
                                                   .CeilingPriority = NULL,
                                                   .Availability = TRUE,
                                                  }
#endif
#if NUMBER_OF_RESOURCES >= 17
                                                  {
                                                   .ResourceProperty = RESOURCE_PROPERTY_17,
                                                   .LinkedResource = (OsResourceContainer *) &RESOURCE_LINKEDRESOURCE_17,
                                                   .CeilingPriority = NULL,
                                                   .Availability = TRUE,
                                                  }
#endif
#if NUMBER_OF_RESOURCES >= 18
                                                  {
                                                   .ResourceProperty = RESOURCE_PROPERTY_18,
                                                   .LinkedResource = (OsResourceContainer *) &RESOURCE_LINKEDRESOURCE_18,
                                                   .CeilingPriority = NULL,
                                                   .Availability = TRUE,
                                                  }
#endif
#if NUMBER_OF_RESOURCES >= 19
                                                  {
                                                   .ResourceProperty = RESOURCE_PROPERTY_19,
                                                   .LinkedResource = (OsResourceContainer *) &RESOURCE_LINKEDRESOURCE_19,
                                                   .CeilingPriority = NULL,
                                                   .Availability = TRUE,
                                                  }
#endif
#if NUMBER_OF_RESOURCES >= 20
                                                  {
                                                   .ResourceProperty = RESOURCE_PROPERTY_20,
                                                   .LinkedResource = (OsResourceContainer *) &RESOURCE_LINKEDRESOURCE_20,
                                                   .CeilingPriority = NULL,
                                                   .Availability = TRUE,
                                                  }
#endif
};

#endif

/* Declaration of ResourcesInTask */
#if NUMBER_OF_EXTENDEDTASK > 0

    #if TASK_1_NUMBER_OF_RES_IN_TASK == 0
        _0_RESOURCES_IN_TASK( 1 );
    #endif
    #if TASK_1_NUMBER_OF_RES_IN_TASK == 1
        _1_RESOURCES_IN_TASK( 1 );
    #endif
    #if TASK_1_NUMBER_OF_RES_IN_TASK == 2
        _2_RESOURCES_IN_TASK( 1 );
    #endif
    #if TASK_1_NUMBER_OF_RES_IN_TASK == 3
        _3_RESOURCES_IN_TASK( 1 );
    #endif
    #if TASK_1_NUMBER_OF_RES_IN_TASK == 4
        _4_RESOURCES_IN_TASK( 1 );
    #endif
    #if TASK_1_NUMBER_OF_RES_IN_TASK == 5
        _5_RESOURCES_IN_TASK( 1 );
    #endif
    #if TASK_1_NUMBER_OF_RES_IN_TASK == 6
        _6_RESOURCES_IN_TASK( 1 );
    #endif
    #if TASK_1_NUMBER_OF_RES_IN_TASK == 7
        _7_RESOURCES_IN_TASK( 1 );
    #endif
    #if TASK_1_NUMBER_OF_RES_IN_TASK == 8
        _8_RESOURCES_IN_TASK( 1 );
    #endif
#if NUMBER_OF_EXTENDEDTASK >= 2
    #if TASK_2_NUMBER_OF_RES_IN_TASK == 0
        _0_RESOURCES_IN_TASK( 2 );
    #endif
    #if TASK_2_NUMBER_OF_RES_IN_TASK == 1
        _1_RESOURCES_IN_TASK( 2 );
    #endif
    #if TASK_2_NUMBER_OF_RES_IN_TASK == 2
        _2_RESOURCES_IN_TASK( 2 );
    #endif
    #if TASK_2_NUMBER_OF_RES_IN_TASK == 3
        _3_RESOURCES_IN_TASK( 2 );
    #endif
    #if TASK_2_NUMBER_OF_RES_IN_TASK == 4
        _4_RESOURCES_IN_TASK( 2 );
    #endif
    #if TASK_2_NUMBER_OF_RES_IN_TASK == 5
        _5_RESOURCES_IN_TASK( 2 );
    #endif
    #if TASK_2_NUMBER_OF_RES_IN_TASK == 6
        _6_RESOURCES_IN_TASK( 2 );
    #endif
    #if TASK_2_NUMBER_OF_RES_IN_TASK == 7
        _7_RESOURCES_IN_TASK( 2 );
    #endif
    #if TASK_2_NUMBER_OF_RES_IN_TASK == 8
        _8_RESOURCES_IN_TASK( 2 );
    #endif
#endif
#if NUMBER_OF_EXTENDEDTASK >= 3
    #if TASK_3_NUMBER_OF_RES_IN_TASK == 0
        _0_RESOURCES_IN_TASK( 3 );
    #endif
    #if TASK_3_NUMBER_OF_RES_IN_TASK == 1
        _1_RESOURCES_IN_TASK( 3 );
    #endif
    #if TASK_3_NUMBER_OF_RES_IN_TASK == 2
        _2_RESOURCES_IN_TASK( 3 );
    #endif
    #if TASK_3_NUMBER_OF_RES_IN_TASK == 3
        _3_RESOURCES_IN_TASK( 3 );
    #endif
    #if TASK_3_NUMBER_OF_RES_IN_TASK == 4
        _4_RESOURCES_IN_TASK( 3 );
    #endif
    #if TASK_3_NUMBER_OF_RES_IN_TASK == 5
        _5_RESOURCES_IN_TASK( 3 );
    #endif
    #if TASK_3_NUMBER_OF_RES_IN_TASK == 6
        _6_RESOURCES_IN_TASK( 3 );
    #endif
    #if TASK_3_NUMBER_OF_RES_IN_TASK == 7
        _7_RESOURCES_IN_TASK( 3 );
    #endif
    #if TASK_3_NUMBER_OF_RES_IN_TASK == 8
        _8_RESOURCES_IN_TASK( 3 );
    #endif
#endif
#if NUMBER_OF_EXTENDEDTASK >= 4
    #if TASK_4_NUMBER_OF_RES_IN_TASK == 0
        _0_RESOURCES_IN_TASK( 4 );
    #endif
    #if TASK_4_NUMBER_OF_RES_IN_TASK == 1
        _1_RESOURCES_IN_TASK( 4 );
    #endif
    #if TASK_4_NUMBER_OF_RES_IN_TASK == 2
        _2_RESOURCES_IN_TASK( 4 );
    #endif
    #if TASK_4_NUMBER_OF_RES_IN_TASK == 3
        _3_RESOURCES_IN_TASK( 4 );
    #endif
    #if TASK_4_NUMBER_OF_RES_IN_TASK == 4
        _4_RESOURCES_IN_TASK( 4 );
    #endif
    #if TASK_4_NUMBER_OF_RES_IN_TASK == 5
        _5_RESOURCES_IN_TASK( 4 );
    #endif
    #if TASK_4_NUMBER_OF_RES_IN_TASK == 6
        _6_RESOURCES_IN_TASK( 4 );
    #endif
    #if TASK_4_NUMBER_OF_RES_IN_TASK == 7
        _7_RESOURCES_IN_TASK( 4 );
    #endif
    #if TASK_4_NUMBER_OF_RES_IN_TASK == 8
        _8_RESOURCES_IN_TASK( 4 );
    #endif
#endif
#if NUMBER_OF_EXTENDEDTASK >= 5
    #if TASK_5_NUMBER_OF_RES_IN_TASK == 0
        _0_RESOURCES_IN_TASK( 5 );
    #endif
    #if TASK_5_NUMBER_OF_RES_IN_TASK == 1
        _1_RESOURCES_IN_TASK( 5 );
    #endif
    #if TASK_5_NUMBER_OF_RES_IN_TASK == 2
        _2_RESOURCES_IN_TASK( 5 );
    #endif
    #if TASK_5_NUMBER_OF_RES_IN_TASK == 3
        _3_RESOURCES_IN_TASK( 5 );
    #endif
    #if TASK_5_NUMBER_OF_RES_IN_TASK == 4
        _4_RESOURCES_IN_TASK( 5 );
    #endif
    #if TASK_5_NUMBER_OF_RES_IN_TASK == 5
        _5_RESOURCES_IN_TASK( 5 );
    #endif
    #if TASK_5_NUMBER_OF_RES_IN_TASK == 6
        _6_RESOURCES_IN_TASK( 5 );
    #endif
    #if TASK_5_NUMBER_OF_RES_IN_TASK == 7
        _7_RESOURCES_IN_TASK( 5 );
    #endif
    #if TASK_5_NUMBER_OF_RES_IN_TASK == 8
        _8_RESOURCES_IN_TASK( 5 );
    #endif
#endif
#if NUMBER_OF_EXTENDEDTASK >= 6
    #if TASK_6_NUMBER_OF_RES_IN_TASK == 0
        _0_RESOURCES_IN_TASK( 6 );
    #endif
    #if TASK_6_NUMBER_OF_RES_IN_TASK == 1
        _1_RESOURCES_IN_TASK( 6 );
    #endif
    #if TASK_6_NUMBER_OF_RES_IN_TASK == 2
        _2_RESOURCES_IN_TASK( 6 );
    #endif
    #if TASK_6_NUMBER_OF_RES_IN_TASK == 3
        _3_RESOURCES_IN_TASK( 6 );
    #endif
    #if TASK_6_NUMBER_OF_RES_IN_TASK == 4
        _4_RESOURCES_IN_TASK( 6 );
    #endif
    #if TASK_6_NUMBER_OF_RES_IN_TASK == 5
        _5_RESOURCES_IN_TASK( 6 );
    #endif
    #if TASK_6_NUMBER_OF_RES_IN_TASK == 6
        _6_RESOURCES_IN_TASK( 6 );
    #endif
    #if TASK_6_NUMBER_OF_RES_IN_TASK == 7
        _7_RESOURCES_IN_TASK( 6 );
    #endif
    #if TASK_6_NUMBER_OF_RES_IN_TASK == 8
        _8_RESOURCES_IN_TASK( 6 );
    #endif
#endif
#if NUMBER_OF_EXTENDEDTASK >= 7
    #if TASK_7_NUMBER_OF_RES_IN_TASK == 0
        _0_RESOURCES_IN_TASK( 7 );
    #endif
    #if TASK_7_NUMBER_OF_RES_IN_TASK == 1
        _1_RESOURCES_IN_TASK( 7 );
    #endif
    #if TASK_7_NUMBER_OF_RES_IN_TASK == 2
        _2_RESOURCES_IN_TASK( 7 );
    #endif
    #if TASK_7_NUMBER_OF_RES_IN_TASK == 3
        _3_RESOURCES_IN_TASK( 7 );
    #endif
    #if TASK_7_NUMBER_OF_RES_IN_TASK == 4
        _4_RESOURCES_IN_TASK( 7 );
    #endif
    #if TASK_7_NUMBER_OF_RES_IN_TASK == 5
        _5_RESOURCES_IN_TASK( 7 );
    #endif
    #if TASK_7_NUMBER_OF_RES_IN_TASK == 6
        _6_RESOURCES_IN_TASK( 7 );
    #endif
    #if TASK_7_NUMBER_OF_RES_IN_TASK == 7
        _7_RESOURCES_IN_TASK( 7 );
    #endif
    #if TASK_7_NUMBER_OF_RES_IN_TASK == 8
        _8_RESOURCES_IN_TASK( 7 );
    #endif
#endif
#if NUMBER_OF_EXTENDEDTASK >= 8
    #if TASK_8_NUMBER_OF_RES_IN_TASK == 0
        _0_RESOURCES_IN_TASK( 8 );
    #endif
    #if TASK_8_NUMBER_OF_RES_IN_TASK == 1
        _1_RESOURCES_IN_TASK( 8 );
    #endif
    #if TASK_8_NUMBER_OF_RES_IN_TASK == 2
        _2_RESOURCES_IN_TASK( 8 );
    #endif
    #if TASK_8_NUMBER_OF_RES_IN_TASK == 3
        _3_RESOURCES_IN_TASK( 8 );
    #endif
    #if TASK_8_NUMBER_OF_RES_IN_TASK == 4
        _4_RESOURCES_IN_TASK( 8 );
    #endif
    #if TASK_8_NUMBER_OF_RES_IN_TASK == 5
        _5_RESOURCES_IN_TASK( 8 );
    #endif
    #if TASK_8_NUMBER_OF_RES_IN_TASK == 6
        _6_RESOURCES_IN_TASK( 8 );
    #endif
    #if TASK_8_NUMBER_OF_RES_IN_TASK == 7
        _7_RESOURCES_IN_TASK( 8 );
    #endif
    #if TASK_8_NUMBER_OF_RES_IN_TASK == 8
        _8_RESOURCES_IN_TASK( 8 );
    #endif
#endif
#if NUMBER_OF_EXTENDEDTASK >= 9
    #if TASK_9_NUMBER_OF_RES_IN_TASK == 0
        _0_RESOURCES_IN_TASK( 9 );
    #endif
    #if TASK_9_NUMBER_OF_RES_IN_TASK == 1
        _1_RESOURCES_IN_TASK( 9 );
    #endif
    #if TASK_9_NUMBER_OF_RES_IN_TASK == 2
        _2_RESOURCES_IN_TASK( 9 );
    #endif
    #if TASK_9_NUMBER_OF_RES_IN_TASK == 3
        _3_RESOURCES_IN_TASK( 9 );
    #endif
    #if TASK_9_NUMBER_OF_RES_IN_TASK == 4
        _4_RESOURCES_IN_TASK( 9 );
    #endif
    #if TASK_9_NUMBER_OF_RES_IN_TASK == 5
        _5_RESOURCES_IN_TASK( 9 );
    #endif
    #if TASK_9_NUMBER_OF_RES_IN_TASK == 6
        _6_RESOURCES_IN_TASK( 9 );
    #endif
    #if TASK_9_NUMBER_OF_RES_IN_TASK == 7
        _7_RESOURCES_IN_TASK( 9 );
    #endif
    #if TASK_9_NUMBER_OF_RES_IN_TASK == 8
        _8_RESOURCES_IN_TASK( 9 );
    #endif
#endif
#if NUMBER_OF_EXTENDEDTASK >= 10
    #if TASK_10_NUMBER_OF_RES_IN_TASK == 0
        _0_RESOURCES_IN_TASK( 10 );
    #endif
    #if TASK_10_NUMBER_OF_RES_IN_TASK == 1
        _1_RESOURCES_IN_TASK( 10 );
    #endif
    #if TASK_10_NUMBER_OF_RES_IN_TASK == 2
        _2_RESOURCES_IN_TASK( 10 );
    #endif
    #if TASK_10_NUMBER_OF_RES_IN_TASK == 3
        _3_RESOURCES_IN_TASK( 10 );
    #endif
    #if TASK_10_NUMBER_OF_RES_IN_TASK == 4
        _4_RESOURCES_IN_TASK( 10 );
    #endif
    #if TASK_10_NUMBER_OF_RES_IN_TASK == 5
        _5_RESOURCES_IN_TASK( 10 );
    #endif
    #if TASK_10_NUMBER_OF_RES_IN_TASK == 6
        _6_RESOURCES_IN_TASK( 10 );
    #endif
    #if TASK_10_NUMBER_OF_RES_IN_TASK == 7
        _7_RESOURCES_IN_TASK( 10 );
    #endif
    #if TASK_10_NUMBER_OF_RES_IN_TASK == 8
        _8_RESOURCES_IN_TASK( 10 );
    #endif
#endif
#endif



#if NUMBER_OF_EVENTS > 0

/* Create Event Handle (ID) for all Events. The handle can be used to
SetEvent, WaitEvent, GetEvent, etc.*/
UBaseType_t const volatile EVENT_NAME_1 = (UBaseType_t) &EVENT_NAME_1;
#if NUMBER_OF_EVENTS >= 2
UBaseType_t const volatile EVENT_NAME_2 = (UBaseType_t) &EVENT_NAME_2;
#endif
#if NUMBER_OF_EVENTS >= 3
UBaseType_t const volatile EVENT_NAME_3 = (UBaseType_t) &EVENT_NAME_3;
#endif
#if NUMBER_OF_EVENTS >= 4
UBaseType_t const volatile EVENT_NAME_4 = (UBaseType_t) &EVENT_NAME_4;
#endif
#if NUMBER_OF_EVENTS >= 5
UBaseType_t const volatile EVENT_NAME_5 = (UBaseType_t) &EVENT_NAME_5;
#endif
#if NUMBER_OF_EVENTS >= 6
UBaseType_t const volatile EVENT_NAME_6 = (UBaseType_t) &EVENT_NAME_6;
#endif
#if NUMBER_OF_EVENTS >= 7
UBaseType_t const volatile EVENT_NAME_7 = (UBaseType_t) &EVENT_NAME_7;
#endif
#if NUMBER_OF_EVENTS >= 8
UBaseType_t const volatile EVENT_NAME_8 = (UBaseType_t) &EVENT_NAME_8;
#endif
#if NUMBER_OF_EVENTS >= 9
UBaseType_t const volatile EVENT_NAME_9 = (UBaseType_t) &EVENT_NAME_9;
#endif
#if NUMBER_OF_EVENTS >= 10
UBaseType_t const volatile EVENT_NAME_10 = (UBaseType_t) &EVENT_NAME_10;
#endif
#if NUMBER_OF_EVENTS >= 11
UBaseType_t const volatile EVENT_NAME_11 = (UBaseType_t) &EVENT_NAME_11;
#endif
#if NUMBER_OF_EVENTS >= 12
UBaseType_t const volatile EVENT_NAME_12 = (UBaseType_t) &EVENT_NAME_12;
#endif
#if NUMBER_OF_EVENTS >= 13
UBaseType_t const volatile EVENT_NAME_13 = (UBaseType_t) &EVENT_NAME_13;
#endif
#if NUMBER_OF_EVENTS >= 14
UBaseType_t const volatile EVENT_NAME_14 = (UBaseType_t) &EVENT_NAME_14;
#endif
#if NUMBER_OF_EVENTS >= 15
UBaseType_t const volatile EVENT_NAME_15 = (UBaseType_t) &EVENT_NAME_15;
#endif
#if NUMBER_OF_EVENTS >= 16
UBaseType_t const volatile EVENT_NAME_16 = (UBaseType_t) &EVENT_NAME_16;
#endif
#if NUMBER_OF_EVENTS >= 17
UBaseType_t const volatile EVENT_NAME_17 = (UBaseType_t) &EVENT_NAME_17;
#endif
#if NUMBER_OF_EVENTS >= 18
UBaseType_t const volatile EVENT_NAME_18 = (UBaseType_t) &EVENT_NAME_18;
#endif
#if NUMBER_OF_EVENTS >= 19
UBaseType_t const volatile EVENT_NAME_19 = (UBaseType_t) &EVENT_NAME_19;
#endif
#if NUMBER_OF_EVENTS >= 20
UBaseType_t const volatile EVENT_NAME_20 = (UBaseType_t) &EVENT_NAME_20;
#endif
#if NUMBER_OF_EVENTS >= 21
UBaseType_t const volatile EVENT_NAME_21 = (UBaseType_t) &EVENT_NAME_21;
#endif
#if NUMBER_OF_EVENTS >= 22
UBaseType_t const volatile EVENT_NAME_22 = (UBaseType_t) &EVENT_NAME_22;
#endif
#if NUMBER_OF_EVENTS >= 23
UBaseType_t const volatile EVENT_NAME_23 = (UBaseType_t) &EVENT_NAME_23;
#endif
#if NUMBER_OF_EVENTS >= 24
UBaseType_t const volatile EVENT_NAME_24 = (UBaseType_t) &EVENT_NAME_24;
#endif
#if NUMBER_OF_EVENTS >= 25
UBaseType_t const volatile EVENT_NAME_25 = (UBaseType_t) &EVENT_NAME_25;
#endif
#if NUMBER_OF_EVENTS >= 26
UBaseType_t const volatile EVENT_NAME_26 = (UBaseType_t) &EVENT_NAME_26;
#endif
#if NUMBER_OF_EVENTS >= 27
UBaseType_t const volatile EVENT_NAME_27 = (UBaseType_t) &EVENT_NAME_27;
#endif
#if NUMBER_OF_EVENTS >= 28
UBaseType_t const volatile EVENT_NAME_28 = (UBaseType_t) &EVENT_NAME_28;
#endif
#if NUMBER_OF_EVENTS >= 29
UBaseType_t const volatile EVENT_NAME_29 = (UBaseType_t) &EVENT_NAME_29;
#endif
#if NUMBER_OF_EVENTS >= 30
UBaseType_t const volatile EVENT_NAME_30 = (UBaseType_t) &EVENT_NAME_30;
#endif

OsEvent EventStruct[NUMBER_OF_EVENTS] = {
                                         {
                                          .Mask = (UBaseType_t) &EventStruct[0],
                                         },
#if NUMBER_OF_EVENTS >= 2
                                         {
                                          .Mask = (UBaseType_t) &EventStruct[1],
                                         },
#endif
#if NUMBER_OF_EVENTS >= 3
                                         {
                                          .Mask = (UBaseType_t) &EventStruct[2],
                                         },
#endif
#if NUMBER_OF_EVENTS >= 4
                                         {
                                          .Mask = (UBaseType_t) &EventStruct[3],
                                         },
#endif
#if NUMBER_OF_EVENTS >= 5
                                         {
                                          .Mask = (UBaseType_t) &EventStruct[4],
                                         },
#endif
#if NUMBER_OF_EVENTS >= 6
                                         {
                                          .Mask = (UBaseType_t) &EventStruct[5],
                                         },
#endif
#if NUMBER_OF_EVENTS >= 7
                                         {
                                          .Mask = (UBaseType_t) &EventStruct[6],
                                         },
#endif
#if NUMBER_OF_EVENTS >= 8
                                         {
                                          .Mask = (UBaseType_t) &EventStruct[7],
                                         },
#endif
#if NUMBER_OF_EVENTS >= 9
                                         {
                                          .Mask = (UBaseType_t) &EventStruct[8],
                                         },
#endif
#if NUMBER_OF_EVENTS >= 10
                                         {
                                          .Mask = (UBaseType_t) &EventStruct[9],
                                         },
#endif
#if NUMBER_OF_EVENTS >= 11
                                         {
                                          .Mask = (UBaseType_t) &EventStruct[10],
                                         },
#endif
#if NUMBER_OF_EVENTS >= 12
                                         {
                                          .Mask = (UBaseType_t) &EventStruct[11],
                                         },
#endif
#if NUMBER_OF_EVENTS >= 13
                                         {
                                          .Mask = (UBaseType_t) &EventStruct[12],
                                         },
#endif
#if NUMBER_OF_EVENTS >= 14
                                         {
                                          .Mask = (UBaseType_t) &EventStruct[13],
                                         },
#endif
#if NUMBER_OF_EVENTS >= 15
                                         {
                                          .Mask = (UBaseType_t) &EventStruct[14],
                                         },
#endif
#if NUMBER_OF_EVENTS >= 16
                                         {
                                          .Mask = (UBaseType_t) &EventStruct[15],
                                         },
#endif
#if NUMBER_OF_EVENTS >= 17
                                         {
                                          .Mask = (UBaseType_t) &EventStruct[16],
                                         },
#endif
#if NUMBER_OF_EVENTS >= 18
                                         {
                                          .Mask = (UBaseType_t) &EventStruct[17],
                                         },
#endif
#if NUMBER_OF_EVENTS >= 19
                                         {
                                          .Mask = (UBaseType_t) &EventStruct[18],
                                         },
#endif
#if NUMBER_OF_EVENTS >= 20
                                         {
                                          .Mask = (UBaseType_t) &EventStruct[19],
                                         },
#endif
#if NUMBER_OF_EVENTS >= 21
                                         {
                                          .Mask = (UBaseType_t) &EventStruct[20],
                                         },
#endif
#if NUMBER_OF_EVENTS >= 22
                                         {
                                          .Mask = (UBaseType_t) &EventStruct[21],
                                         },
#endif
#if NUMBER_OF_EVENTS >= 23
                                         {
                                          .Mask = (UBaseType_t) &EventStruct[22],
                                         },
#endif
#if NUMBER_OF_EVENTS >= 24
                                         {
                                          .Mask = (UBaseType_t) &EventStruct[23],
                                         },
#endif
#if NUMBER_OF_EVENTS >= 25
                                         {
                                          .Mask = (UBaseType_t) &EventStruct[24],
                                         },
#endif
#if NUMBER_OF_EVENTS >= 26
                                         {
                                          .Mask = (UBaseType_t) &EventStruct[25],
                                         },
#endif
#if NUMBER_OF_EVENTS >= 27
                                         {
                                          .Mask = (UBaseType_t) &EventStruct[26],
                                         },
#endif
#if NUMBER_OF_EVENTS >= 28
                                         {
                                          .Mask = (UBaseType_t) &EventStruct[27],
                                         },
#endif
#if NUMBER_OF_EVENTS >= 29
                                         {
                                          .Mask = (UBaseType_t) &EventStruct[28],
                                         },
#endif
#if NUMBER_OF_EVENTS >= 30
                                         {
                                          .Mask = (UBaseType_t) &EventStruct[29],
                                         },
#endif
};
#endif


#if NUMBER_OF_EVENTS > 0
TaskEventsRef EventsInTask[NUMBER_OF_EXTENDEDTASK] = {
                                                      {
                                                       .event1 = (UBaseType_t) &TASK_1_EVENT_1,
                                                       .event2 = (UBaseType_t) &TASK_1_EVENT_2,
                                                       .event3 = (UBaseType_t) &TASK_1_EVENT_3,
                                                       .event4 = (UBaseType_t) &TASK_1_EVENT_4,
                                                       .event5 = (UBaseType_t) &TASK_1_EVENT_5,
                                                       .event6 = (UBaseType_t) &TASK_1_EVENT_6,
                                                       .event7 = (UBaseType_t) &TASK_1_EVENT_7,
                                                       .event8 = (UBaseType_t) &TASK_1_EVENT_8,
                                                      },
#if NUMBER_OF_EXTENDEDTASK >= 2
                                                      {
                                                       .event1 = (UBaseType_t) &TASK_2_EVENT_1,
                                                       .event2 = (UBaseType_t) &TASK_2_EVENT_2,
                                                       .event3 = (UBaseType_t) &TASK_2_EVENT_3,
                                                       .event4 = (UBaseType_t) &TASK_2_EVENT_4,
                                                       .event5 = (UBaseType_t) &TASK_2_EVENT_5,
                                                       .event6 = (UBaseType_t) &TASK_2_EVENT_6,
                                                       .event7 = (UBaseType_t) &TASK_2_EVENT_7,
                                                       .event8 = (UBaseType_t) &TASK_2_EVENT_8,
                                                      },
#endif
#if NUMBER_OF_EXTENDEDTASK >= 3
                                                      {
                                                       .event1 = (UBaseType_t) &TASK_3_EVENT_1,
                                                       .event2 = (UBaseType_t) &TASK_3_EVENT_2,
                                                       .event3 = (UBaseType_t) &TASK_3_EVENT_3,
                                                       .event4 = (UBaseType_t) &TASK_3_EVENT_4,
                                                       .event5 = (UBaseType_t) &TASK_3_EVENT_5,
                                                       .event6 = (UBaseType_t) &TASK_3_EVENT_6,
                                                       .event7 = (UBaseType_t) &TASK_3_EVENT_7,
                                                       .event8 = (UBaseType_t) &TASK_3_EVENT_8,
                                                      },
#endif
#if NUMBER_OF_EXTENDEDTASK >= 4
                                                      {
                                                       .event1 = (UBaseType_t) &TASK_4_EVENT_1,
                                                       .event2 = (UBaseType_t) &TASK_4_EVENT_2,
                                                       .event3 = (UBaseType_t) &TASK_4_EVENT_3,
                                                       .event4 = (UBaseType_t) &TASK_4_EVENT_4,
                                                       .event5 = (UBaseType_t) &TASK_4_EVENT_5,
                                                       .event6 = (UBaseType_t) &TASK_4_EVENT_6,
                                                       .event7 = (UBaseType_t) &TASK_4_EVENT_7,
                                                       .event8 = (UBaseType_t) &TASK_4_EVENT_8,
                                                      },
#endif
#if NUMBER_OF_EXTENDEDTASK >= 5
                                                      {
                                                       .event1 = (UBaseType_t) &TASK_5_EVENT_1,
                                                       .event2 = (UBaseType_t) &TASK_5_EVENT_2,
                                                       .event3 = (UBaseType_t) &TASK_5_EVENT_3,
                                                       .event4 = (UBaseType_t) &TASK_5_EVENT_4,
                                                       .event5 = (UBaseType_t) &TASK_5_EVENT_5,
                                                       .event6 = (UBaseType_t) &TASK_5_EVENT_6,
                                                       .event7 = (UBaseType_t) &TASK_5_EVENT_7,
                                                       .event8 = (UBaseType_t) &TASK_5_EVENT_8,
                                                      },
#endif
#if NUMBER_OF_EXTENDEDTASK >= 6
                                                      {
                                                       .event1 = (UBaseType_t) &TASK_6_EVENT_1,
                                                       .event2 = (UBaseType_t) &TASK_6_EVENT_2,
                                                       .event3 = (UBaseType_t) &TASK_6_EVENT_3,
                                                       .event4 = (UBaseType_t) &TASK_6_EVENT_4,
                                                       .event5 = (UBaseType_t) &TASK_6_EVENT_5,
                                                       .event6 = (UBaseType_t) &TASK_6_EVENT_6,
                                                       .event7 = (UBaseType_t) &TASK_6_EVENT_7,
                                                       .event8 = (UBaseType_t) &TASK_6_EVENT_8,
                                                      },
#endif
#if NUMBER_OF_EXTENDEDTASK >= 7
                                                      {
                                                       .event1 = (UBaseType_t) &TASK_7_EVENT_1,
                                                       .event2 = (UBaseType_t) &TASK_7_EVENT_2,
                                                       .event3 = (UBaseType_t) &TASK_7_EVENT_3,
                                                       .event4 = (UBaseType_t) &TASK_7_EVENT_4,
                                                       .event5 = (UBaseType_t) &TASK_7_EVENT_5,
                                                       .event6 = (UBaseType_t) &TASK_7_EVENT_6,
                                                       .event7 = (UBaseType_t) &TASK_7_EVENT_7,
                                                       .event8 = (UBaseType_t) &TASK_7_EVENT_8,
                                                      },
#endif
#if NUMBER_OF_EXTENDEDTASK >= 8
                                                      {
                                                       .event1 = (UBaseType_t) &TASK_8_EVENT_1,
                                                       .event2 = (UBaseType_t) &TASK_8_EVENT_2,
                                                       .event3 = (UBaseType_t) &TASK_8_EVENT_3,
                                                       .event4 = (UBaseType_t) &TASK_8_EVENT_4,
                                                       .event5 = (UBaseType_t) &TASK_8_EVENT_5,
                                                       .event6 = (UBaseType_t) &TASK_8_EVENT_6,
                                                       .event7 = (UBaseType_t) &TASK_8_EVENT_7,
                                                       .event8 = (UBaseType_t) &TASK_8_EVENT_8,
                                                      },
#endif
};
#endif

/******************************* Task Struct *********************************************/

/* declare Task stack for each task */

static StackType_t IdleStack[IDLETASK_STACK_SIZE];
#if NUMBER_OF_TASKS >= 1
static StackType_t TaskStack1[TASK_SIZE_1];
#endif
#if NUMBER_OF_TASKS >= 2
static StackType_t TaskStack2[TASK_SIZE_2];
#endif
#if NUMBER_OF_TASKS >= 3
static StackType_t TaskStack3[TASK_SIZE_3];
#endif
#if NUMBER_OF_TASKS >= 4
static StackType_t TaskStack4[TASK_SIZE_4];
#endif
#if NUMBER_OF_TASKS >= 5
static StackType_t TaskStack5[TASK_SIZE_5];
#endif
#if NUMBER_OF_TASKS >= 6
static StackType_t TaskStack6[TASK_SIZE_6];
#endif
#if NUMBER_OF_TASKS >= 7
static StackType_t TaskStack7[TASK_SIZE_7];
#endif
#if NUMBER_OF_TASKS >= 8
static StackType_t TaskStack8[TASK_SIZE_8];
#endif
#if NUMBER_OF_TASKS >= 9
static StackType_t TaskStack9[TASK_SIZE_9];
#endif
#if NUMBER_OF_TASKS >= 10
static StackType_t TaskStack10[TASK_SIZE_10];
#endif
#if NUMBER_OF_TASKS >= 11
static StackType_t TaskStack11[TASK_SIZE_11];
#endif
#if NUMBER_OF_TASKS >= 12
static StackType_t TaskStack12[TASK_SIZE_12];
#endif
#if NUMBER_OF_TASKS >= 13
static StackType_t TaskStack13[TASK_SIZE_13];
#endif
#if NUMBER_OF_TASKS >= 14
static StackType_t TaskStack14[TASK_SIZE_14];
#endif
#if NUMBER_OF_TASKS >= 15
static StackType_t TaskStack15[TASK_SIZE_15];
#endif
#if NUMBER_OF_TASKS >= 16
static StackType_t TaskStack16[TASK_SIZE_16];
#endif
#if NUMBER_OF_TASKS >= 17
static StackType_t TaskStack17[TASK_SIZE_17];
#endif
#if NUMBER_OF_TASKS >= 18
static StackType_t TaskStack18[TASK_SIZE_18];
#endif
#if NUMBER_OF_TASKS >= 19
static StackType_t TaskStack19[TASK_SIZE_19];
#endif
#if NUMBER_OF_TASKS >= 20
static StackType_t TaskStack20[TASK_SIZE_20];
#endif


OsTask TaskStruct[NUMBER_OF_TASKS + 1] = {
                                          {
                                           .StackRef = IdleStack,
                                           .StackSize = IDLETASK_STACK_SIZE,
                                           .TaskCode = (TaskFunction_t) IdleTask,
                                           .Priority = NULL,
                                           .StartingPriority = NULL,
                                           .Activation = 1,
                                           .Schedule = FULL,
                                           .AutoStart = TRUE,
                                           .TaskType = BASIC,
                                          },
#if NUMBER_OF_TASKS >= 1
                                          {
                                           .StackRef = TaskStack1,
                                           .StackSize = TASK_SIZE_1,
                                           .TaskCode = (TaskFunction_t) TASK_FUNCTION_NAME(TASK_NAME_1),
                                           .Priority =  TASK_Priority_1,
                                           .StartingPriority = TASK_Priority_1,
                                           .Activation = TASK_ACTIVATION_1,
                                           .Schedule = TASK_SCHEDULE_1,
                                           .AutoStart = TASK_AUTOSTART_1,
                                           .TaskType = TASK_TYPE_1,
                                          },
#endif
#if NUMBER_OF_TASKS >= 2
                                          {
                                           .StackRef = TaskStack2,
                                           .StackSize = TASK_SIZE_2,
                                           .TaskCode = (TaskFunction_t) TASK_FUNCTION_NAME(TASK_NAME_2),
                                           .Priority = TASK_Priority_2,
                                           .StartingPriority = TASK_Priority_2,
                                           .Activation = TASK_ACTIVATION_2,
                                           .Schedule = TASK_SCHEDULE_2,
                                           .AutoStart = TASK_AUTOSTART_2,
                                           .TaskType = TASK_TYPE_2,
                                          },
#endif
#if NUMBER_OF_TASKS >= 3
                                          {
                                           .StackRef = TaskStack3,
                                           .StackSize = TASK_SIZE_3,
                                           .TaskCode = (TaskFunction_t) TASK_FUNCTION_NAME(TASK_NAME_3),
                                           .Priority = TASK_Priority_3,
                                           .StartingPriority = TASK_Priority_3,
                                           .Activation = TASK_ACTIVATION_3,
                                           .Schedule = TASK_SCHEDULE_3,
                                           .AutoStart = TASK_AUTOSTART_3,
                                           .TaskType = TASK_TYPE_3,
                                          },
#endif
#if NUMBER_OF_TASKS >= 4
                                          {
                                           .StackRef = TaskStack4,
                                           .StackSize = TASK_SIZE_4,
                                           .TaskCode = (TaskFunction_t) TASK_FUNCTION_NAME(TASK_NAME_4),
                                           .Priority = TASK_Priority_4,
                                           .StartingPriority = TASK_Priority_4,
                                           .Activation = TASK_ACTIVATION_4,
                                           .Schedule = TASK_SCHEDULE_4,
                                           .AutoStart = TASK_AUTOSTART_4,
                                           .TaskType = TASK_TYPE_4,
                                          },
#endif
#if NUMBER_OF_TASKS >= 5
                                          {
                                           .StackRef = TaskStack5,
                                           .StackSize = TASK_SIZE_5,
                                           .TaskCode = (TaskFunction_t) TASK_FUNCTION_NAME(TASK_NAME_5),
                                           .Priority = TASK_Priority_5,
                                           .StartingPriority = TASK_Priority_5,
                                           .Activation = TASK_ACTIVATION_5,
                                           .Schedule = TASK_SCHEDULE_5,
                                           .AutoStart = TASK_AUTOSTART_5,
                                           .TaskType = TASK_TYPE_5,
                                          },
#endif
#if NUMBER_OF_TASKS >= 6
                                          {
                                           .StackRef = TaskStack6,
                                           .StackSize = TASK_SIZE_6,
                                           .TaskCode = (TaskFunction_t) TASK_FUNCTION_NAME(TASK_NAME_6),
                                           .Priority = TASK_Priority_6,
                                           .StartingPriority = TASK_Priority_6,
                                           .Activation = TASK_ACTIVATION_6,
                                           .Schedule = TASK_SCHEDULE_6,
                                           .AutoStart = TASK_AUTOSTART_6,
                                           .TaskType = TASK_TYPE_6,
                                          },
#endif
#if NUMBER_OF_TASKS >= 7
                                          {
                                           .StackRef = TaskStack7,
                                           .StackSize = TASK_SIZE_7,
                                           .TaskCode = (TaskFunction_t) TASK_FUNCTION_NAME(TASK_NAME_7),
                                           .Priority = TASK_Priority_7,
                                           .StartingPriority = TASK_Priority_7,
                                           .Activation = TASK_ACTIVATION_7,
                                           .Schedule = TASK_SCHEDULE_7,
                                           .AutoStart = TASK_AUTOSTART_7,
                                           .TaskType = TASK_TYPE_7,
                                          },
#endif
#if NUMBER_OF_TASKS >= 8
                                          {
                                           .StackRef = TaskStack8,
                                           .StackSize = TASK_SIZE_8,
                                           .TaskCode = (TaskFunction_t) TASK_FUNCTION_NAME(TASK_NAME_8),
                                           .Priority = TASK_Priority_8,
                                           .StartingPriority = TASK_Priority_8,
                                           .Activation = TASK_ACTIVATION_8,
                                           .Schedule = TASK_SCHEDULE_8,
                                           .AutoStart = TASK_AUTOSTART_8,
                                           .TaskType = TASK_TYPE_8,
                                          },
#endif
#if NUMBER_OF_TASKS >= 9
                                          {
                                           .StackRef = TaskStack9,
                                           .StackSize = TASK_SIZE_9,
                                           .TaskCode = (TaskFunction_t) TASK_FUNCTION_NAME(TASK_NAME_9),
                                           .Priority = TASK_Priority_9,
                                           .StartingPriority = TASK_Priority_9,
                                           .Activation = TASK_ACTIVATION_9,
                                           .Schedule = TASK_SCHEDULE_9,
                                           .AutoStart = TASK_AUTOSTART_9,
                                           .TaskType = TASK_TYPE_9,
                                          },
#endif
#if NUMBER_OF_TASKS >= 10
                                          {
                                           .StackRef = TaskStack10,
                                           .StackSize = TASK_SIZE_10,
                                           .TaskCode = (TaskFunction_t) TASK_FUNCTION_NAME(TASK_NAME_10),
                                           .Priority = TASK_Priority_10,
                                           .StartingPriority = TASK_Priority_10,
                                           .Activation = TASK_ACTIVATION_10,
                                           .Schedule = TASK_SCHEDULE_10,
                                           .AutoStart = TASK_AUTOSTART_10,
                                           .TaskType = TASK_TYPE_10,
                                          },
#endif
#if NUMBER_OF_TASKS >= 11
                                          {
                                           .StackRef = TaskStack11,
                                           .StackSize = TASK_SIZE_11,
                                           .TaskCode = (TaskFunction_t) TASK_FUNCTION_NAME(TASK_NAME_11),
                                           .Priority = TASK_Priority_11,
                                           .StartingPriority = TASK_Priority_11,
                                           .Activation = TASK_ACTIVATION_11,
                                           .Schedule = TASK_SCHEDULE_11,
                                           .AutoStart = TASK_AUTOSTART_11,
                                           .TaskType = TASK_TYPE_11,
                                          },
#endif
#if NUMBER_OF_TASKS >= 12
                                          {
                                           .StackRef = TaskStack12,
                                           .StackSize = TASK_SIZE_12,
                                           .TaskCode = (TaskFunction_t) TASK_FUNCTION_NAME(TASK_NAME_12),
                                           .Priority = TASK_Priority_12,
                                           .StartingPriority = TASK_Priority_12,
                                           .Activation = TASK_ACTIVATION_12,
                                           .Schedule = TASK_SCHEDULE_12,
                                           .AutoStart = TASK_AUTOSTART_12,
                                           .TaskType = TASK_TYPE_12,
                                          },
#endif
#if NUMBER_OF_TASKS >= 13
                                          {
                                           .StackRef = TaskStack13,
                                           .StackSize = TASK_SIZE_13,
                                           .TaskCode = (TaskFunction_t) TASK_FUNCTION_NAME(TASK_NAME_13),
                                           .Priority = TASK_Priority_13,
                                           .StartingPriority = TASK_Priority_13,
                                           .Activation = TASK_ACTIVATION_13,
                                           .Schedule = TASK_SCHEDULE_13,
                                           .AutoStart = TASK_AUTOSTART_13,
                                           .TaskType = TASK_TYPE_13,
                                          },
#endif
#if NUMBER_OF_TASKS >= 14
                                          {
                                           .StackRef = TaskStack14,
                                           .StackSize = TASK_SIZE_14,
                                           .TaskCode = (TaskFunction_t) TASK_FUNCTION_NAME(TASK_NAME_14),
                                           .Priority = TASK_Priority_14,
                                           .StartingPriority = TASK_Priority_14,
                                           .Activation = TASK_ACTIVATION_14,
                                           .Schedule = TASK_SCHEDULE_14,
                                           .AutoStart = TASK_AUTOSTART_14,
                                           .TaskType = TASK_TYPE_14,
                                          },
#endif
#if NUMBER_OF_TASKS >= 15
                                          {
                                           .StackRef = TaskStack15,
                                           .StackSize = TASK_SIZE_15,
                                           .TaskCode = (TaskFunction_t) TASK_FUNCTION_NAME(TASK_NAME_15),
                                           .Priority = TASK_Priority_15,
                                           .StartingPriority = TASK_Priority_15,
                                           .Activation = TASK_ACTIVATION_15,
                                           .Schedule = TASK_SCHEDULE_15,
                                           .AutoStart = TASK_AUTOSTART_15,
                                           .TaskType = TASK_TYPE_15,
                                          },
#endif
#if NUMBER_OF_TASKS >= 16
                                          {
                                           .StackRef = TaskStack16,
                                           .StackSize = TASK_SIZE_16,
                                           .TaskCode = (TaskFunction_t) TASK_FUNCTION_NAME(TASK_NAME_16),
                                           .Priority = TASK_Priority_16,
                                           .StartingPriority = TASK_Priority_16,
                                           .Activation = TASK_ACTIVATION_16,
                                           .Schedule = TASK_SCHEDULE_16,
                                           .AutoStart = TASK_AUTOSTART_16,
                                           .TaskType = TASK_TYPE_16,
                                          },
#endif
#if NUMBER_OF_TASKS >= 17
                                          {
                                           .StackRef = TaskStack17,
                                           .StackSize = TASK_SIZE_17,
                                           .TaskCode = (TaskFunction_t) TASK_FUNCTION_NAME(TASK_NAME_17),
                                           .Priority = TASK_Priority_17,
                                           .StartingPriority = TASK_Priority_17,
                                           .Activation = TASK_ACTIVATION_17,
                                           .Schedule = TASK_SCHEDULE_17,
                                           .AutoStart = TASK_AUTOSTART_17,
                                           .TaskType = TASK_TYPE_17,
                                          },
#endif
#if NUMBER_OF_TASKS >= 18
                                          {
                                           .StackRef = TaskStack18,
                                           .StackSize = TASK_SIZE_18,
                                           .TaskCode = (TaskFunction_t) TASK_FUNCTION_NAME(TASK_NAME_18),
                                           .Priority = TASK_Priority_18,
                                           .StartingPriority = TASK_Priority_18,
                                           .Activation = TASK_ACTIVATION_18,
                                           .Schedule = TASK_SCHEDULE_18,
                                           .AutoStart = TASK_AUTOSTART_18,
                                           .TaskType = TASK_TYPE_18,
                                          },
#endif
#if NUMBER_OF_TASKS >= 19
                                          {
                                           .StackRef = TaskStack19,
                                           .StackSize = TASK_SIZE_19,
                                           .TaskCode = (TaskFunction_t) TASK_FUNCTION_NAME(TASK_NAME_19),
                                           .Priority = TASK_Priority_19,
                                           .StartingPriority = TASK_Priority_19,
                                           .Activation = TASK_ACTIVATION_19,
                                           .Schedule = TASK_SCHEDULE_19,
                                           .AutoStart = TASK_AUTOSTART_19,
                                           .TaskType = TASK_TYPE_19,
                                          },
#endif
#if NUMBER_OF_TASKS >= 20
                                          {
                                           .StackRef = TaskStack20,
                                           .StackSize = TASK_SIZE_20,
                                           .TaskCode = (TaskFunction_t) TASK_FUNCTION_NAME(TASK_NAME_20),
                                           .Priority = TASK_Priority_20,
                                           .StartingPriority = TASK_Priority_20,
                                           .Activation = TASK_ACTIVATION_20,
                                           .Schedule = TASK_SCHEDULE_20,
                                           .AutoStart = TASK_AUTOSTART_20,
                                           .TaskType = TASK_TYPE_20,
                                          },
#endif
};

/* Create Task Handle (ID) for all Tasks. The handle can be used to
ActivateTask, ChainTask, GetTaskState etc.*/

#if NUMBER_OF_TASKS >= 1
TaskType const TASK_NAME_1 = (TaskType) &TaskStruct[1];
#endif
#if NUMBER_OF_TASKS >= 2
TaskType const TASK_NAME_2 = (TaskType) &TaskStruct[2];
#endif
#if NUMBER_OF_TASKS >= 3
TaskType const TASK_NAME_3 = (TaskType) &TaskStruct[3];
#endif
#if NUMBER_OF_TASKS >= 4
TaskType const TASK_NAME_4 = (TaskType) &TaskStruct[4];
#endif
#if NUMBER_OF_TASKS >= 5
TaskType const TASK_NAME_5 = (TaskType) &TaskStruct[5];
#endif
#if NUMBER_OF_TASKS >= 6
TaskType const TASK_NAME_6 = (TaskType) &TaskStruct[6];
#endif
#if NUMBER_OF_TASKS >= 7
TaskType const TASK_NAME_7 = (TaskType) &TaskStruct[7];
#endif
#if NUMBER_OF_TASKS >= 8
TaskType const TASK_NAME_8 = (TaskType) &TaskStruct[8];
#endif
#if NUMBER_OF_TASKS >= 9
TaskType const TASK_NAME_9 = (TaskType) &TaskStruct[9];
#endif
#if NUMBER_OF_TASKS >= 10
TaskType const TASK_NAME_10 = (TaskType) &TaskStruct[10];
#endif
#if NUMBER_OF_TASKS >= 11
TaskType const TASK_NAME_11 = (TaskType) &TaskStruct[11];
#endif
#if NUMBER_OF_TASKS >= 12
TaskType const TASK_NAME_12 = (TaskType) &TaskStruct[12];
#endif
#if NUMBER_OF_TASKS >= 13
TaskType const TASK_NAME_13 = (TaskType) &TaskStruct[13];
#endif
#if NUMBER_OF_TASKS >= 14
TaskType const TASK_NAME_14 = (TaskType) &TaskStruct[14];
#endif
#if NUMBER_OF_TASKS >= 15
TaskType const TASK_NAME_15 = (TaskType) &TaskStruct[15];
#endif
#if NUMBER_OF_TASKS >= 16
TaskType const TASK_NAME_16 = (TaskType) &TaskStruct[16];
#endif
#if NUMBER_OF_TASKS >= 17
TaskType const TASK_NAME_17 = (TaskType) &TaskStruct[17];
#endif
#if NUMBER_OF_TASKS >= 18
TaskType const TASK_NAME_18 = (TaskType) &TaskStruct[18];
#endif
#if NUMBER_OF_TASKS >= 19
TaskType const TASK_NAME_19 = (TaskType) &TaskStruct[19];
#endif
#if NUMBER_OF_TASKS >= 20
TaskType const TASK_NAME_20 = (TaskType) &TaskStruct[20];
#endif

/***************************** Counter Structs ***************************************/

#if NUMBER_OF_COUNTER
OsCounter CounterStruct[NUMBER_OF_COUNTER] = {
#if NUMBER_OF_COUNTER >= 1
                                              {
                                               .MaxAllowedValue = COUNTER_MAX_ALLOWED_VALUE_1,
                                               .TicksPerBase = COUNTER_TICKS_PER_BASE_1,
                                               .MinCycle = COUNTER_MIN_CYCLE_1,
                                              },
#endif
#if NUMBER_OF_COUNTER >= 2
                                              {
                                               .MaxAllowedValue = COUNTER_MAX_ALLOWED_VALUE_2,
                                               .TicksPerBase = COUNTER_TICKS_PER_BASE_2,
                                               .MinCycle = COUNTER_MIN_CYCLE_2,
                                              },
#endif
#if NUMBER_OF_COUNTER >= 3
                                              {
                                               .MaxAllowedValue = COUNTER_MAX_ALLOWED_VALUE_3,
                                               .TicksPerBase = COUNTER_TICKS_PER_BASE_3,
                                               .MinCycle = COUNTER_MIN_CYCLE_3,
                                              },
#endif
#if NUMBER_OF_COUNTER >= 4
                                              {
                                               .MaxAllowedValue = COUNTER_MAX_ALLOWED_VALUE_4,
                                               .TicksPerBase = COUNTER_TICKS_PER_BASE_4,
                                               .MinCycle = COUNTER_MIN_CYCLE_4,
                                              },
#endif
#if NUMBER_OF_COUNTER >= 5
                                              {
                                               .MaxAllowedValue = COUNTER_MAX_ALLOWED_VALUE_5,
                                               .TicksPerBase = COUNTER_TICKS_PER_BASE_5,
                                               .MinCycle = COUNTER_MIN_CYCLE_5,
                                              },
#endif
#if NUMBER_OF_COUNTER >= 6
                                              {
                                               .MaxAllowedValue = COUNTER_MAX_ALLOWED_VALUE_6,
                                               .TicksPerBase = COUNTER_TICKS_PER_BASE_6,
                                               .MinCycle = COUNTER_MIN_CYCLE_6,
                                              },
#endif
#if NUMBER_OF_COUNTER >= 7
                                              {
                                               .MaxAllowedValue = COUNTER_MAX_ALLOWED_VALUE_7,
                                               .TicksPerBase = COUNTER_TICKS_PER_BASE_7,
                                               .MinCycle = COUNTER_MIN_CYCLE_7,
                                              },
#endif
#if NUMBER_OF_COUNTER >= 8
                                              {
                                               .MaxAllowedValue = COUNTER_MAX_ALLOWED_VALUE_8,
                                               .TicksPerBase = COUNTER_TICKS_PER_BASE_8,
                                               .MinCycle = COUNTER_MIN_CYCLE_8,
                                              },
#endif
#if NUMBER_OF_COUNTER >= 9
                                              {
                                               .MaxAllowedValue = COUNTER_MAX_ALLOWED_VALUE_9,
                                               .TicksPerBase = COUNTER_TICKS_PER_BASE_9,
                                               .MinCycle = COUNTER_MIN_CYCLE_9,
                                              },
#endif
#if NUMBER_OF_COUNTER >= 10
                                              {
                                               .MaxAllowedValue = COUNTER_MAX_ALLOWED_VALUE_10,
                                               .TicksPerBase = COUNTER_TICKS_PER_BASE_10,
                                               .MinCycle = COUNTER_MIN_CYCLE_10,
                                              },
#endif
};
#endif


/***************************** Alarm Structs ***************************************/

#if NUMBER_OF_ALARM != 0
OsAlarm AlarmStruct[NUMBER_OF_ALARM] = {
                                        {
                                         .pCounterID = (OsCounter *) &CounterStruct[ALARM_COUNTER_1],
                                         .Action = ALARM_ACTION_1,
                                         .TaskID = (UBaseType_t *) &ALARM_ACTION_TASKID_1,
#if ALARM_ACTION_1 == SETEVENT
                                         .EventID = (UBaseType_t *) &ALARM_ACTION_EVENTID_1,
#endif
                                         .AlarmTime = ALARM_AUTOSTART_ALARMTIME_1 - 1,
                                         .CycleTime = ALARM_AUTOSTART_CYCLETIME_1,
                                         .AutoStart = ALARM_AUTOSTART_1,
                                        #if ALARM_CALLBACK
                                         .AlarmCallBackFunc = (AlarmCallBackFunction_t) ALARM_CALLBACK_FUNCTION_1,
                                        #endif
                                        },
#if NUMBER_OF_ALARM >= 2
                                        {
                                         .pCounterID = (OsCounter *) &CounterStruct[ALARM_COUNTER_2],
                                         .Action = ALARM_ACTION_2,
                                         .TaskID = (UBaseType_t *) &ALARM_ACTION_TASKID_2,
#if ALARM_ACTION_2 == SETEVENT
                                         .EventID = (UBaseType_t *) &ALARM_ACTION_EVENTID_2,
#endif
                                         .AlarmTime = ALARM_AUTOSTART_ALARMTIME_2 - 1,
                                         .CycleTime = ALARM_AUTOSTART_CYCLETIME_2,
                                         .AutoStart = ALARM_AUTOSTART_2,
                                        #if ALARM_CALLBACK
                                         .AlarmCallBackFunc = (AlarmCallBackFunction_t) ALARM_CALLBACK_FUNCTION_2,
                                        #endif
                                        },
#endif
#if NUMBER_OF_ALARM >= 3
                                        {
                                         .pCounterID = (OsCounter *) &CounterStruct[ALARM_COUNTER_3],
                                         .Action = ALARM_ACTION_3,
                                         .TaskID = (UBaseType_t *) &ALARM_ACTION_TASKID_3,
#if ALARM_ACTION_3 == SETEVENT
                                         .EventID = (UBaseType_t *) &ALARM_ACTION_EVENTID_3,
#endif
                                         .AlarmTime = ALARM_AUTOSTART_ALARMTIME_3 - 1,
                                         .CycleTime = ALARM_AUTOSTART_CYCLETIME_3,
                                         .AutoStart = ALARM_AUTOSTART_3,
                                        #if ALARM_CALLBACK
                                         .AlarmCallBackFunc = (AlarmCallBackFunction_t) ALARM_CALLBACK_FUNCTION_3,
                                        #endif
                                        },
#endif
#if NUMBER_OF_ALARM >= 4
                                        {
                                         .pCounterID = (OsCounter *) &CounterStruct[ALARM_COUNTER_4],
                                         .Action = ALARM_ACTION_4,
                                         .TaskID = (UBaseType_t *) &ALARM_ACTION_TASKID_4,
#if ALARM_ACTION_4 == SETEVENT
                                         .EventID = (UBaseType_t *) &ALARM_ACTION_EVENTID_4,
#endif
                                         .AlarmTime = ALARM_AUTOSTART_ALARMTIME_4 - 1,
                                         .CycleTime = ALARM_AUTOSTART_CYCLETIME_4,
                                         .AutoStart = ALARM_AUTOSTART_4,
                                        #if ALARM_CALLBACK
                                         .AlarmCallBackFunc = (AlarmCallBackFunction_t) ALARM_CALLBACK_FUNCTION_4,
                                        #endif
                                        },
#endif
#if NUMBER_OF_ALARM >= 5
                                        {
                                         .pCounterID = (OsCounter *) &CounterStruct[ALARM_COUNTER_5],
                                         .Action = ALARM_ACTION_5,
                                         .TaskID = (UBaseType_t *) &ALARM_ACTION_TASKID_5,
#if ALARM_ACTION_5 == SETEVENT
                                         .EventID = (UBaseType_t *) &ALARM_ACTION_EVENTID_5,
#endif
                                         .AlarmTime = ALARM_AUTOSTART_ALARMTIME_5 - 1,
                                         .CycleTime = ALARM_AUTOSTART_CYCLETIME_5,
                                         .AutoStart = ALARM_AUTOSTART_5,
                                        #if ALARM_CALLBACK
                                         .AlarmCallBackFunc = (AlarmCallBackFunction_t) ALARM_CALLBACK_FUNCTION_5,
                                        #endif
                                        },
#endif
#if NUMBER_OF_ALARM >= 6
                                        {
                                         .pCounterID = (OsCounter *) &CounterStruct[ALARM_COUNTER_6],
                                         .Action = ALARM_ACTION_6,
                                         .TaskID = (UBaseType_t *) &ALARM_ACTION_TASKID_6,
#if ALARM_ACTION_6 == SETEVENT
                                         .EventID = (UBaseType_t *) &ALARM_ACTION_EVENTID_6,
#endif
                                         .AlarmTime = ALARM_AUTOSTART_ALARMTIME_6 - 1,
                                         .CycleTime = ALARM_AUTOSTART_CYCLETIME_6,
                                         .AutoStart = ALARM_AUTOSTART_6,
                                        #if ALARM_CALLBACK
                                         .AlarmCallBackFunc = (AlarmCallBackFunction_t) ALARM_CALLBACK_FUNCTION_6,
                                        #endif
                                        },
#endif
#if NUMBER_OF_ALARM >= 7
                                        {
                                         .pCounterID = (OsCounter *) &CounterStruct[ALARM_COUNTER_7],
                                         .Action = ALARM_ACTION_7,
                                         .TaskID = (UBaseType_t *) &ALARM_ACTION_TASKID_7,
#if ALARM_ACTION_7 == SETEVENT
                                         .EventID = (UBaseType_t *) &ALARM_ACTION_EVENTID_7,
#endif
                                         .AlarmTime = ALARM_AUTOSTART_ALARMTIME_7 - 1,
                                         .CycleTime = ALARM_AUTOSTART_CYCLETIME_7,
                                         .AutoStart = ALARM_AUTOSTART_7,
                                        #if ALARM_CALLBACK
                                         .AlarmCallBackFunc = (AlarmCallBackFunction_t) ALARM_CALLBACK_FUNCTION_7,
                                        #endif
                                        },
#endif
#if NUMBER_OF_ALARM >= 8
                                        {
                                         .pCounterID = (OsCounter *) &CounterStruct[ALARM_COUNTER_8],
                                         .Action = ALARM_ACTION_8,
                                         .TaskID = (UBaseType_t *) &ALARM_ACTION_TASKID_8,
#if ALARM_ACTION_8 == SETEVENT
                                         .EventID = (UBaseType_t *) &ALARM_ACTION_EVENTID_8,
#endif
                                         .AlarmTime = ALARM_AUTOSTART_ALARMTIME_8 - 1,
                                         .CycleTime = ALARM_AUTOSTART_CYCLETIME_8,
                                         .AutoStart = ALARM_AUTOSTART_8,
                                        #if ALARM_CALLBACK
                                         .AlarmCallBackFunc = (AlarmCallBackFunction_t) ALARM_CALLBACK_FUNCTION_8,
                                        #endif
                                        },
#endif
#if NUMBER_OF_ALARM >= 9
                                        {
                                         .pCounterID = (OsCounter *) &CounterStruct[ALARM_COUNTER_9],
                                         .Action = ALARM_ACTION_9,
                                         .TaskID = (UBaseType_t *) &ALARM_ACTION_TASKID_9,
#if ALARM_ACTION_9 == SETEVENT
                                         .EventID = (UBaseType_t *) &ALARM_ACTION_EVENTID_9,
#endif
                                         .AlarmTime = ALARM_AUTOSTART_ALARMTIME_9 - 1,
                                         .CycleTime = ALARM_AUTOSTART_CYCLETIME_9,
                                         .AutoStart = ALARM_AUTOSTART_9,
                                        #if ALARM_CALLBACK
                                         .AlarmCallBackFunc = (AlarmCallBackFunction_t) ALARM_CALLBACK_FUNCTION_9,
                                        #endif
                                        },
#endif
#if NUMBER_OF_ALARM >= 10
                                        {
                                         .pCounterID = (OsCounter *) &CounterStruct[ALARM_COUNTER_10],
                                         .Action = ALARM_ACTION_10,
                                         .TaskID = (UBaseType_t *) &ALARM_ACTION_TASKID_10,
#if ALARM_ACTION_10 == SETEVENT
                                         .EventID = (UBaseType_t *) &ALARM_ACTION_EVENTID_10,
#endif
                                         .AlarmTime = ALARM_AUTOSTART_ALARMTIME_10 - 1,
                                         .CycleTime = ALARM_AUTOSTART_CYCLETIME_10,
                                         .AutoStart = ALARM_AUTOSTART_10,
                                        #if ALARM_CALLBACK
                                         .AlarmCallBackFunc = (AlarmCallBackFunction_t) ALARM_CALLBACK_FUNCTION_10,
                                        #endif
                                        },
#endif
#if NUMBER_OF_ALARM >= 11
                                        {
                                         .pCounterID = (OsCounter *) &CounterStruct[ALARM_COUNTER_11],
                                         .Action = ALARM_ACTION_11,
                                         .TaskID = (UBaseType_t *) &ALARM_ACTION_TASKID_11,
#if ALARM_ACTION_11 == SETEVENT
                                         .EventID = (UBaseType_t *) &ALARM_ACTION_EVENTID_11,
#endif
                                         .AlarmTime = ALARM_AUTOSTART_ALARMTIME_11 - 1,
                                         .CycleTime = ALARM_AUTOSTART_CYCLETIME_11,
                                         .AutoStart = ALARM_AUTOSTART_11,
                                        #if ALARM_CALLBACK
                                         .AlarmCallBackFunc = (AlarmCallBackFunction_t) ALARM_CALLBACK_FUNCTION_11,
                                        #endif
                                        },
#endif
#if NUMBER_OF_ALARM >= 12
                                        {
                                         .pCounterID = (OsCounter *) &CounterStruct[ALARM_COUNTER_12],
                                         .Action = ALARM_ACTION_12,
                                         .TaskID = (UBaseType_t *) &ALARM_ACTION_TASKID_12,
#if ALARM_ACTION_12 == SETEVENT
                                         .EventID = (UBaseType_t *) &ALARM_ACTION_EVENTID_12,
#endif
                                         .AlarmTime = ALARM_AUTOSTART_ALARMTIME_12 - 1,
                                         .CycleTime = ALARM_AUTOSTART_CYCLETIME_12,
                                         .AutoStart = ALARM_AUTOSTART_12,
                                        #if ALARM_CALLBACK
                                         .AlarmCallBackFunc = (AlarmCallBackFunction_t) ALARM_CALLBACK_FUNCTION_12,
                                        #endif
                                        },
#endif
#if NUMBER_OF_ALARM >= 13
                                        {
                                         .pCounterID = (OsCounter *) &CounterStruct[ALARM_COUNTER_13],
                                         .Action = ALARM_ACTION_13,
                                         .TaskID = (UBaseType_t *) &ALARM_ACTION_TASKID_13,
#if ALARM_ACTION_13 == SETEVENT
                                         .EventID = (UBaseType_t *) &ALARM_ACTION_EVENTID_13,
#endif
                                         .AlarmTime = ALARM_AUTOSTART_ALARMTIME_13 - 1,
                                         .CycleTime = ALARM_AUTOSTART_CYCLETIME_13,
                                         .AutoStart = ALARM_AUTOSTART_13,
                                        #if ALARM_CALLBACK
                                         .AlarmCallBackFunc = (AlarmCallBackFunction_t) ALARM_CALLBACK_FUNCTION_13,
                                        #endif
                                        },
#endif
#if NUMBER_OF_ALARM >= 14
                                        {
                                         .pCounterID = (OsCounter *) &CounterStruct[ALARM_COUNTER_14],
                                         .Action = ALARM_ACTION_14,
                                         .TaskID = (UBaseType_t *) &ALARM_ACTION_TASKID_14,
#if ALARM_ACTION_14 == SETEVENT
                                         .EventID = (UBaseType_t *) &ALARM_ACTION_EVENTID_14,
#endif
                                         .AlarmTime = ALARM_AUTOSTART_ALARMTIME_14 - 1,
                                         .CycleTime = ALARM_AUTOSTART_CYCLETIME_14,
                                         .AutoStart = ALARM_AUTOSTART_14,
                                        #if ALARM_CALLBACK
                                         .AlarmCallBackFunc = (AlarmCallBackFunction_t) ALARM_CALLBACK_FUNCTION_14,
                                        #endif
                                        },
#endif
#if NUMBER_OF_ALARM >= 15
                                        {
                                         .pCounterID = (OsCounter *) &CounterStruct[ALARM_COUNTER_15],
                                         .Action = ALARM_ACTION_15,
                                         .TaskID = (UBaseType_t *) &ALARM_ACTION_TASKID_15,
#if ALARM_ACTION_15 == SETEVENT
                                         .EventID = (UBaseType_t *) &ALARM_ACTION_EVENTID_15,
#endif
                                         .AlarmTime = ALARM_AUTOSTART_ALARMTIME_15 - 1,
                                         .CycleTime = ALARM_AUTOSTART_CYCLETIME_15,
                                         .AutoStart = ALARM_AUTOSTART_15,
                                        #if ALARM_CALLBACK
                                         .AlarmCallBackFunc = (AlarmCallBackFunction_t) ALARM_CALLBACK_FUNCTION_15,
                                        #endif
                                        },
#endif
#if NUMBER_OF_ALARM >= 16
                                        {
                                         .pCounterID = (OsCounter *) &CounterStruct[ALARM_COUNTER_16],
                                         .Action = ALARM_ACTION_16,
                                         .TaskID = (UBaseType_t *) &ALARM_ACTION_TASKID_16,
#if ALARM_ACTION_16 == SETEVENT
                                         .EventID = (UBaseType_t *) &ALARM_ACTION_EVENTID_16,
#endif
                                         .AlarmTime = ALARM_AUTOSTART_ALARMTIME_16 - 1,
                                         .CycleTime = ALARM_AUTOSTART_CYCLETIME_16,
                                         .AutoStart = ALARM_AUTOSTART_16,
                                        #if ALARM_CALLBACK
                                         .AlarmCallBackFunc = (AlarmCallBackFunction_t) ALARM_CALLBACK_FUNCTION_16,
                                        #endif
                                        },
#endif
#if NUMBER_OF_ALARM >= 17
                                        {
                                         .pCounterID = (OsCounter *) &CounterStruct[ALARM_COUNTER_17],
                                         .Action = ALARM_ACTION_17,
                                         .TaskID = (UBaseType_t *) &ALARM_ACTION_TASKID_17,
#if ALARM_ACTION_17 == SETEVENT
                                         .EventID = (UBaseType_t *) &ALARM_ACTION_EVENTID_17,
#endif
                                         .AlarmTime = ALARM_AUTOSTART_ALARMTIME_17 - 1,
                                         .CycleTime = ALARM_AUTOSTART_CYCLETIME_17,
                                         .AutoStart = ALARM_AUTOSTART_17,
                                        #if ALARM_CALLBACK
                                         .AlarmCallBackFunc = (AlarmCallBackFunction_t) ALARM_CALLBACK_FUNCTION_17,
                                        #endif
                                        },
#endif
#if NUMBER_OF_ALARM >= 18
                                        {
                                         .pCounterID = (OsCounter *) &CounterStruct[ALARM_COUNTER_18],
                                         .Action = ALARM_ACTION_18,
                                         .TaskID = (UBaseType_t *) &ALARM_ACTION_TASKID_18,
#if ALARM_ACTION_18 == SETEVENT
                                         .EventID = (UBaseType_t *) &ALARM_ACTION_EVENTID_18,
#endif
                                         .AlarmTime = ALARM_AUTOSTART_ALARMTIME_18 - 1,
                                         .CycleTime = ALARM_AUTOSTART_CYCLETIME_18,
                                         .AutoStart = ALARM_AUTOSTART_18,
                                        #if ALARM_CALLBACK
                                         .AlarmCallBackFunc = (AlarmCallBackFunction_t) ALARM_CALLBACK_FUNCTION_18,
                                        #endif
                                        },
#endif
#if NUMBER_OF_ALARM >= 19
                                        {
                                         .pCounterID = (OsCounter *) &CounterStruct[ALARM_COUNTER_19],
                                         .Action = ALARM_ACTION_19,
                                         .TaskID = (UBaseType_t *) &ALARM_ACTION_TASKID_19,
#if ALARM_ACTION_19 == SETEVENT
                                         .EventID = (UBaseType_t *) &ALARM_ACTION_EVENTID_19,
#endif
                                         .AlarmTime = ALARM_AUTOSTART_ALARMTIME_19 - 1,
                                         .CycleTime = ALARM_AUTOSTART_CYCLETIME_19,
                                         .AutoStart = ALARM_AUTOSTART_19,
                                        #if ALARM_CALLBACK
                                         .AlarmCallBackFunc = (AlarmCallBackFunction_t) ALARM_CALLBACK_FUNCTION_19,
                                        #endif
                                        },
#endif
#if NUMBER_OF_ALARM >= 20
                                        {
                                         .pCounterID = (OsCounter *) &CounterStruct[ALARM_COUNTER_20],
                                         .Action = ALARM_ACTION_20,
                                         .TaskID = (UBaseType_t *) &ALARM_ACTION_TASKID_20,
#if ALARM_ACTION_20 == SETEVENT
                                         .EventID = (UBaseType_t *) &ALARM_ACTION_EVENTID_20,
#endif
                                         .AlarmTime = ALARM_AUTOSTART_ALARMTIME_20 - 1,
                                         .CycleTime = ALARM_AUTOSTART_CYCLETIME_20,
                                         .AutoStart = ALARM_AUTOSTART_20,
                                        #if ALARM_CALLBACK
                                         .AlarmCallBackFunc = (AlarmCallBackFunction_t) ALARM_CALLBACK_FUNCTION_20,
                                        #endif
                                        },
#endif
};
#endif

#if NUMBER_OF_ALARM >= 1
AlarmType const ALARM_NAME_1 = (AlarmType) &AlarmStruct[0];
#endif
#if NUMBER_OF_ALARM >= 2
AlarmType const ALARM_NAME_2 = (AlarmType) &AlarmStruct[1];
#endif
#if NUMBER_OF_ALARM >= 3
AlarmType const ALARM_NAME_3 = (AlarmType) &AlarmStruct[2];
#endif
#if NUMBER_OF_ALARM >= 4
AlarmType const ALARM_NAME_4 = (AlarmType) &AlarmStruct[3];
#endif
#if NUMBER_OF_ALARM >= 5
AlarmType const ALARM_NAME_5 = (AlarmType) &AlarmStruct[4];
#endif
#if NUMBER_OF_ALARM >= 6
AlarmType const ALARM_NAME_6 = (AlarmType) &AlarmStruct[5];
#endif
#if NUMBER_OF_ALARM >= 7
AlarmType const ALARM_NAME_7 = (AlarmType) &AlarmStruct[6];
#endif
#if NUMBER_OF_ALARM >= 8
AlarmType const ALARM_NAME_8 = (AlarmType) &AlarmStruct[7];
#endif
#if NUMBER_OF_ALARM >= 9
AlarmType const ALARM_NAME_9 = (AlarmType) &AlarmStruct[8];
#endif
#if NUMBER_OF_ALARM >= 10
AlarmType const ALARM_NAME_10 = (AlarmType) &AlarmStruct[9];
#endif
#if NUMBER_OF_ALARM >= 11
AlarmType const ALARM_NAME_11 = (AlarmType) &AlarmStruct[10];
#endif
#if NUMBER_OF_ALARM >= 12
AlarmType const ALARM_NAME_12 = (AlarmType) &AlarmStruct[11];
#endif
#if NUMBER_OF_ALARM >= 13
AlarmType const ALARM_NAME_13 = (AlarmType) &AlarmStruct[12];
#endif
#if NUMBER_OF_ALARM >= 14
AlarmType const ALARM_NAME_14 = (AlarmType) &AlarmStruct[13];
#endif
#if NUMBER_OF_ALARM >= 15
AlarmType const ALARM_NAME_15 = (AlarmType) &AlarmStruct[14];
#endif
#if NUMBER_OF_ALARM >= 16
AlarmType const ALARM_NAME_16 = (AlarmType) &AlarmStruct[15];
#endif
#if NUMBER_OF_ALARM >= 17
AlarmType const ALARM_NAME_17 = (AlarmType) &AlarmStruct[16];
#endif
#if NUMBER_OF_ALARM >= 18
AlarmType const ALARM_NAME_18 = (AlarmType) &AlarmStruct[17];
#endif
#if NUMBER_OF_ALARM >= 19
AlarmType const ALARM_NAME_19 = (AlarmType) &AlarmStruct[18];
#endif
#if NUMBER_OF_ALARM >= 20
AlarmType const ALARM_NAME_20 = (AlarmType) &AlarmStruct[19];
#endif
