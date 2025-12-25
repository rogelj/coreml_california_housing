//
//  ContentView.swift
//  CaliforniaPricer
//
//  Created by J. Rogel on 25/12/2025.
//

import SwiftUI

struct ContentView: View {
    @State var popUpVisible: Bool = false
    @State var pickerIncome = 0
      
    @State var pickerRoom = 0
    let incomeData = Array(stride(from:0.05, through: 14, by: 0.5))
    let roomData = Array(2...10)
    var body: some View {
        VStack {
            Text("California Pricer").font(.largeTitle)
        }
        .padding()
        HStack {
            Text("Median Income (USD)").padding(.trailing, 10)
            Text("No. of  Rooms").padding(.leading, 10)
        }
        .padding(.vertical, 40)
        Button(action: {
            self.popUpVisible.toggle()
        }) {
            Text("Get Prediction")
        }
        .alert(isPresented: self.$popUpVisible) {
            Alert(title: Text("Prediction"),
            message: Text("Prediction will be shown here."),
                  dismissButton: .default(Text("Cool!"))
                  
            )
        }
    }
}

#Preview {
    ContentView()
}
