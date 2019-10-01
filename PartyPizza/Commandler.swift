//
//  Commandler.swift
//  PartyPizza
//
//  Created by nithin muthukumar on 2019-09-29.
//  Copyright © 2019 nithin muthukumar. All rights reserved.
//

import Foundation
class Commandler{
    static func makePost(name:String,param:String){
        let todoEndpoint: String = "http://34.67.102.175:8888/command"
          guard let url = URL(string: todoEndpoint) else {
            print("Error: cannot create URL")
            return
          }
        var urlRequest = URLRequest(url: url)
        urlRequest.httpMethod="POST"
        
        
        let jsonData = try? JSONSerialization.data(withJSONObject: param)
        urlRequest.httpBody=jsonData

        
          // set up the session
        let config = URLSessionConfiguration.default
        let session = URLSession(configuration: config)
          // make the request
        let task = session.dataTask(with: urlRequest)
    task.resume()
        
    }
    
    static func makePost(_ message:[String:Any])->[[String:Any]]{
        var res:[[String:Any]]=[[String:Any]]()
        
        
            let todoEndpoint: String = "http://34.67.102.175:8888/command"
              guard let url = URL(string: todoEndpoint) else {
                print("Error: cannot create URL")
                return res
                
                
                
              }
            var urlRequest = URLRequest(url: url)
            urlRequest.httpMethod="POST"
            
            
            let jsonData = try? JSONSerialization.data(withJSONObject: message)
            urlRequest.httpBody=jsonData
            let config = URLSessionConfiguration.default
            let session = URLSession(configuration: config)
            let task = session.dataTask(with: urlRequest)
        task.resume()
        return res
        
            
        }

    

    static func makeGetCall() {
        // Set up the URL request
          let todoEndpoint: String = "http://34.67.102.175:8888/hostparty"
          guard let url = URL(string: todoEndpoint) else {
            print("Error: cannot create URL")
            return
          }
          let urlRequest = URLRequest(url: url)
          // set up the session
          let config = URLSessionConfiguration.default
          let session = URLSession(configuration: config)
          // make the request
          let task = session.dataTask(with: urlRequest) {
            (data, response, error) in
            // check for any errors
            guard error == nil else {
              print(error)
              return
            }
            guard let responseData = data else {
              print("Error: did not receive data")
              return
            }
            do {
              guard let todo = try JSONSerialization.jsonObject(with: responseData, options: []) as? [String: AnyObject] else {
                print("error trying to convert data to JSON")
                return
              }
              print("The todo is: " + todo.description)
              guard let todoTitle = todo["title"] as? String else {
                print("Could not get todo title from JSON")
                return
              }
              print("The title is: " + todoTitle)
            } catch  {
              print("error trying to convert data to JSON")
              return
            }
          }
          task.resume()
    }
}
