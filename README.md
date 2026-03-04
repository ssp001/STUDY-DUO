## Study-Duo👨‍🏫
---

### **Frontend**

1. **Student Portal**

   * **Study Interface** – for students to interact with learning content.
   * **Progress Dashboard** – tracks student progress and performance.
   * Sends **study requests** to the backend and receives **personalized guidance** and **performance reports**.

2. **Teacher Portal**

   * **Analytics Dashboard** – visualizes student performance and trends.
   * **Report Generator** – creates performance reports.
   * Sends **analytics requests** to the backend and receives **performance reports**.

---

### **Backend**

1. **MCP Agent**

   * **Request Router** – handles incoming requests from both portals.
   * **Context Manager** – maintains session or context information.
   * Forwards requests to AI Services for processing.

2. **AI Services**

   * **Recommendation Engine** – processes requests and generates suggestions.
   * **Resource Suggester** – recommends learning resources.
   * **Performance Tracker** – monitors progress using student metrics from data storage.

3. **Data Storage**

   * **Student Records** – stores user information and history.
   * **Performance Metrics** – stores grades, engagement, and other performance indicators.
   * **Learning Resources** – stores educational content for recommendations.

---

### **Data Flow**

* Students request guidance → routed via MCP → AI Services process → suggestions returned.
* Teachers request analytics → routed via MCP → AI Services generate reports → returned to teachers.
* AI Services continuously monitor progress and read/write metrics to Data Storage.

---

