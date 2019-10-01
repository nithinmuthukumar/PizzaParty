//
//  MakePartyController.swift
//  PartyPizza
//
//  Created by nithin muthukumar on 2019-09-28.
//  Copyright © 2019 nithin muthukumar. All rights reserved.
//

import UIKit
class MakePartyController: UIViewController,UITextFieldDelegate {
    @IBOutlet weak var PartyField: UITextField!

    @IBAction func CreateParty(_ sender: Any) {
        Globals.partyName=PartyField.text
        
    }
    override func viewDidLoad() {
        super.viewDidLoad()
        PartyField.delegate=self
        // Do any additional setup after loading the view.
    }
    

    func textFieldShouldReturn(_ textField: UITextField) -> Bool {
        textField.resignFirstResponder()
        return true
    }

}
