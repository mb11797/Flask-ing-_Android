package com.example.MB.simpleapp.retrofit

import com.google.gson.GsonBuilder
import com.google.gson.JsonObject
import okhttp3.ResponseBody
import retrofit2.Call
import retrofit2.Retrofit
import retrofit2.converter.gson.GsonConverterFactory
import retrofit2.http.*


/**
 *
 * Created by Manas and Harshita on 29/06/2018.
 */

class APIKindaStuff {

    interface APIService {
        @GET("/users/{user}")
        fun greetUser(@Path("user") user: String): Call<ResponseBody>

        @Headers("Content-type: application/json")
        @POST("/api/post_some_data")
        fun getVectors(@Body body: JsonObject): Call<ResponseBody>
    }

    companion object {
        private val retrofit = Retrofit.Builder()
                .baseUrl("http://10.244.1.42:5000")
                .addConverterFactory(GsonConverterFactory.create(GsonBuilder().create()))
                .build()

        var service = retrofit.create(APIService::class.java)
    }
}